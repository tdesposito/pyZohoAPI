# This file is part of pyZohoAPI, Copyright (C) Todd D. Esposito 2021.
# Distributed under the MIT License (see https://opensource.org/licenses/MIT).

import datetime
import logging
from time import sleep

import requests
import simplejson

from .collection import DottedDict, DottedList
from .utils import diff
from ..exceptions import *

logging.getLogger('pyzohoapi').addHandler(logging.NullHandler())

class ZohoAPIBase:
    _regionmap = {
        'australia': "com.au",
        'com.au': "com.au",
        'com': "com",
        'eu': "eu",
        'europe': "eu",
        'in': "in",
        'india': "in",
        'us': "com",
    }
    def __init__(self, organization_id, region="us", **apiArgs):
        """ Constructor

        :param organization_id: Zoho Organization ID to which to connect
        :type organization_id: str
        :param region: Zoho Data Center Region. Defaults to "us".
        :type region: str
        :param **apiArgs: additional parameters for API operation.
        :raises ZohoUnknownRegionException: if the region is unknown or invalid.

        """
        region = region.lower()
        if region not in self._regionmap:
            raise ZohoUnknownRegionException(region)
        self._org = organization_id
        self._endpoint = self.get_endpoint(region)
        self._oauth = f"https://accounts.zoho.{self._regionmap[region]}/oauth/v2"
        self._ratelimit = {
            'limit': None,
            'NextCall': datetime.datetime.now().timestamp(),
            'remaining': 99999999,
            'reset': None,
        }
        self._api_keys = {
            'access_token': None,
            'client_id': None,
            'client_secret': None,
            'intercall_delay': 0,
            'max_retries': 10,
            'max_retry_after': 180,
            'min_calls_remaining': 1,
            'redirect_url': None,
            'refresh_token': None,
            'retry_backoff_seconds': 0.5,
        }
        self.update_tokens(apiArgs)
        self._logger = logging.getLogger('pyzohoapi')

    def auth_header(self):
        """ Returns the authorization header, refreshing the access_token as needed.

        :return: {'Authorization': '... access token ...'}
        :raises ZohoAuthRefreshFailure: if a refresh attemp fails.
        :raises ZohoInsufficentAuthKeys: if we don't have enough info to refresh.
        """
        if self._api_keys.get('access_token') and self._api_keys['AccessExpiresAt'] > datetime.datetime.now().timestamp():
            return {'Authorization': f"Zoho-oauthtoken {self._api_keys['access_token']}"}
        if self._api_keys.get('refresh_token'):
            self.log("requesting new access token")
            rsp = requests.post(f"{self._oauth}/token", params={
                'refresh_token': self._api_keys['refresh_token'],
                'client_id': self._api_keys['client_id'],
                'client_secret': self._api_keys['client_secret'],
                'redirect_url': self._api_keys['redirect_url'],
                'grant_type': "refresh_token"
            })
            if rsp.ok:
                self.update_tokens(rsp.json())
                return {'Authorization': f"Zoho-oauthtoken {self._api_keys['access_token']}"}
            raise ZohoAuthRefreshFailure()
        raise ZohoInsufficentAuthKeys()

    def do_request(self, requestFunc, url, body=None, files=None):
        if self._api_keys['min_calls_remaining'] >= int(self._ratelimit['remaining']):
            if self._ratelimit['ResetAt'] > datetime.datetime.now():
                self.log("API call limit exceeded")
                raise ZohoAPICallsExceeded()

        now = datetime.datetime.now().timestamp()
        if now < self._ratelimit['NextCall']:
            self.log("pausing for internal API rate limit")
            sleep(self._ratelimit['NextCall'] - now)

        retries = self._api_keys['max_retries']
        while True:
            reqparams = {
                'headers': self.auth_header(),
                'files': files,
                'data': simplejson.dumps(body) if body else None,
            }
            rsp = requestFunc(url, **reqparams)
            self._ratelimit['NextCall'] = datetime.datetime.now().timestamp() + self._api_keys['intercall_delay']
            if rsp.status_code == 429 and retries:  # Too Many Requests
                retries -= 1
                sleeptime = int(rsp.headers.get('retry-after', self._api_keys['retry_backoff_seconds']))
                if sleeptime <= self._api_keys['max_retry_after']:
                    self.log("pausing before retry")
                    sleep(sleeptime)
                else:
                    raise ZohoAPIThrottled()
            elif not rsp.ok:
                err_params = {
                    'code': rsp.status_code,
                    'url': url,
                    'msg': f"Encountered #{rsp.status_code} error calling Zoho API",
                }
                if rsp.headers.get('content-type',"").startswith("application/json"):
                    d = rsp.json()
                    err_params.update({'zoho_code': d.get('code'), 'zoho_msg': d.get('message',"")})
                if rsp.status_code == 401:
                    self._api_keys['access_token'] = None
                    retries -= 1
                    if retries:
                        continue
                raise {
                    '400': ZohoBadRequest,
                    '401': ZohoUnauthorized,
                    '404': ZohoNotFound,
                    '405': ZohoMethodNotAllowed,
                }.get(str(rsp.status_code), ZohoException)(**err_params)
            else:
                if rsp.headers['content-type'].startswith("application/json"):
                    d = rsp.json()
                    if d.get('code') == 0:
                        self.update_rate_limit(rsp.headers)
                        return rsp
                    elif d.get('code') == "43" and retries:    # Throttled
                        retries -= 1
                        sleeptime = int(rsp.headers.get('retry-after', self._api_keys['retry_backoff_seconds']))
                        if sleeptime <= self._api_keys['max_retry_after']:
                            self.log("pausing before retry")
                            sleep(sleeptime)
                        else:
                            raise ZohoAPIThrottled()
                else:
                    return rsp

    def delete(self, urlFragment):
        url = f"{self._endpoint}/{urlFragment}?organization_id={self._org}"
        self.log(f"DELETE {url}")
        rsp = self.do_request(requests.delete, url)
        return rsp.ok

    def get(self, urlFragment, queryString):
        url = f"{self._endpoint}/{urlFragment}?organization_id={self._org}&{queryString}"
        self.log(f"GET {url}")
        rsp = self.do_request(requests.get, url)
        if rsp.headers['content-type'].startswith("application/json"):
            data = simplejson.loads(rsp.text, use_decimal=True)
            if data['code'] == 0:
                return data
            raise ZohoException(f"zoho returned {data['code']}: {data['message']}")
        return DottedDict({
            'content': rsp.content,
            'content_type': rsp.headers['content-type'],
        })

    def get_endpoint(self, region):
        # This MUST be overridden in subclasses for the APIs to work.
        # It's only here in the base class for testing
        return False

    def log(self, message, level=logging.DEBUG):
        self._logger.log(level, f"{self.__class__.__name__} (Org# {self._org}): {message}")

    def post(self, urlFragment, data=None, queryString="", files=None):
        url = f"{self._endpoint}/{urlFragment}?organization_id={self._org}&{queryString}"
        self.log(f"POST {url}")
        rsp = self.do_request(requests.post, url, data, files)
        if rsp.headers['content-type'].startswith("application/json"):
            data = simplejson.loads(rsp.text, use_decimal=True)
            if data['code'] == 0:
                return data
            raise ZohoException(f"zoho returned {data['code']}: {data['message']}")
        return {
            'content': rsp.content,
            'content_type': rsp.headers['content-type'],
        }

    def put(self, urlFragment, data, queryString):
        url = f"{self._endpoint}/{urlFragment}?organization_id={self._org}&{queryString}"
        self.log(f"PUT {url}")
        rsp = self.do_request(requests.put, url, data)
        if rsp.headers['content-type'].startswith("application/json"):
            data = simplejson.loads(rsp.text, use_decimal=True)
            if data['code'] == 0:
                return data
            raise ZohoException(f"zoho returned {data['code']}: {data['message']}")
        return {
            'content': rsp.content,
            'content_type': rsp.headers['content-type'],
        }

    def update_rate_limit(self, headers):
        for key in ['limit', 'reset', 'remaining']:
            if headers.get(f'x-rate-limit-{key}'):
                self._ratelimit[key] = headers[f'x-rate-limit-{key}']
        self._ratelimit['ResetAt'] = datetime.datetime.now() + datetime.timedelta(seconds=int(self._ratelimit.get('reset', 0)))

    def update_tokens(self, apiArgs):
        self._api_keys.update(apiArgs)
        # we subtract a few ticks from our expiry time, to cushion against drift
        self._api_keys['AccessExpiresAt'] = datetime.datetime.now().timestamp() + int(apiArgs.get('expires_in', 0)) - 10


class ZohoObjectBase:
    ID = property(lambda self: self._id)
    IsDeleted = property(lambda self: self._id is False)
    IsList = property(lambda self: isinstance(self._data, DottedList))
    IsLoaded = property(lambda self: self._data is not None)
    Number = property(lambda self: self._data[self._number_field] if isinstance(self._data, DottedDict) else None)

    def __init__(self, api, id=None, **searchParams):
        self._id = id
        self._api = api
        self._data = None
        self._nextpage = None
        if id or {k:v for k,v in searchParams.items() if isinstance(v, str)}:
            try:
                self._load(id=id, **searchParams)
            except ZohoNotFound as e:
                pass    # not found, but no need to raise this error.

    def __iter__(self):
        return self.Iter()

    def __getattr__(self, key):
        if self._data:
            return self._data[key]
        return None

    def __repr__(self):
        if self._id:
            return f"{self.__class__.__name__} #{self._id}"
        if isinstance(self._data, DottedList):
            return f"List of {self.__class__.__name__} objects"
        return f"New {self.__class__.__name__}"

    def __setattr__(self, key, value):
        if key.startswith('_'):
            super().__setattr__(key, value)
        else:
            if not self._data:
                self._data = DottedDict()
            self._data[key] = value

    def _load(self, page=None, **searchParams):
        data = self._api.get(self._url_fragment(), self._query_string(**searchParams))
        if data is None:
            self._data = None
        elif self._id and self._is_raw:
            self._data = DottedDict(data)
        else:
            if self._id:
                self._reload(data)
            else:
                if page:
                    self._data.extend(DottedList(data.get(self._plural)))
                else:
                    self._data = DottedList(data.get(self._plural))
                if data.get('page_context',{}).get('has_more_page'):
                    self._searchParams = searchParams
                    self._nextpage = data['page_context']['page'] + 1
                else:
                    self._nextpage = None

    @staticmethod
    def _passes_filter(obj, filterFunc=None, **filters):
        """ Utility function for filtering object lists
        """
        if filterFunc and not filterFunc(obj):
            return False
        for k,v in filters.items():
            if k in obj and obj[k] != v:
                return False
        return True

    def _query_string(self, **queryArgs):
        qs = "&".join([f"{k}={v}" for (k,v) in queryArgs.items() if v])
        if self._nextpage:
            qs += f"&page={self._nextpage}"
        return qs

    def _reload(self, data):
        self._orig = data.get(self._singular)
        self._data = DottedDict(self._orig)
        self._id = self._data.get(self._id_field)

    def _url_fragment(self, id=None, extraPath=[]):
        if self._id or id:
            return f"{self._type}/{id if id else self._id}/{'/'.join(extraPath)}"
        else:
            return self._type

    def get(self, key, default=None):
        if self._id:
            return self._data.get(key, default)
        return default

    def Create(self, **qParams):
        """ Create this object in Zoho

        :return: `self` as created by Zoho
        :raises ZohoInvalidOpError: if `self` isn't "new"
        """
        if not self._id:
            newData = self._api.post(self._url_fragment(), self._data.to_python(), self._query_string(**qParams))
            if newData:
                self._reload(newData)
            return self
        raise ZohoInvalidOpError("Create", self)

    def Delete(self):
        """ Delete this object from Zoho

        :return: `self`
        :raises ZohoInvalidOpError: if `self` isn't "single-object"
        """
        if self._id:
            if self._api.delete(self._url_fragment()):
                self._id = False
                self._data[self._id_field] = None
            return self
        raise ZohoInvalidOpError("Delete", self)

    def First(self, **kwargs):
        """ Get the first ZohoObject from the list.

        If kwargs are provided, they are used to filter what counts as "first."

        :return: a ZohoObject
        """
        if self._data == None:
            # We were a "new" object, but need to become a list-of
            self._load()
        if isinstance(self._data, DottedList) and len(self._data):
            if kwargs:
                rval = None
                for _ in self.Iter(raw=True, **kwargs): rval = _; break;
                if rval:
                    return self.__class__(self._api, rval[self._id_field])
            else:
                return self.__class__(self._api, self._data[0][self._id_field])
        return self.__class__(self._api)

    def GetRelated(self, targetType, key):
        if self._id and self._data:
            if isinstance(self._data.get(key), str):
                return targetType(self._data[key])
        raise ZohoInvalidOpError("GetRelated", self)

    def Iter(self, filterFunc=None, raw=False, **filter):
        """ Iterate over the list of ZohoObjects

        If called on a non-connected ("new") object, we get the list of ALL objects

        :param filterFunc: function which takes the item to test, returning True or False
        :param raw: return the raw list data?
        :param filter: fields/values to filter the list by
        :return: iterable of ZohoObjects (technically, a generator)
        """
        if self._id:
            return [self]
        if not self.IsLoaded:
            self._load()

        if self.IsLoaded:
            start = 0
            while start < len(self._data) or self._nextpage:
                if start >= len(self._data):
                    self._load(page=self._nextpage, **self._searchParams)

                item = self._data[start]
                if self._passes_filter(item, filterFunc=filterFunc, **filter):
                    if raw:
                        yield item
                    else:
                        yield self.__class__(self._api, id=item[self._id_field])
                start += 1
        else:
            return []

    def IterRelatedList(self, targetType, listKey, idField):
        if self._id and self._data:
            for item in self._data.get(listKey, []):
                yield targetType(item.get(idField))
        else:
            raise ZohoInvalidOpError("IterRelatedList", self)

    def MapRelatedList(self, targetType, listKey, idField):
        if self._id and self._data:
            for item in self._data.get(listKey, []):
                yield DottedDict({'meta': item.to_python(), 'object': targetType(item.get(idField))})
        else:
            raise ZohoInvalidOpError("MapRelatedList", self)

    def Update(self):
        if self._id and self._data:
            updated = diff(self._orig, self._data.to_python())
            if updated:
                data = self._api.put(self._url_fragment(), updated, "")
                self._reload(data)
            return self
        raise ZohoInvalidOpError("Update", self)
