# This file is part of pyZohoAPI, Copyright (C) Todd D. Esposito 2021.
# Distributed under the MIT License (see https://opensource.org/licenses/MIT).

import datetime

import requests

from .collection import DottedDict, DottedList
from .utils import diff
from ..exceptions import *

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
        """Short summary.

        :param organization_id: Description of parameter `organization_id`.
        :type organization_id: type
        :param region: Description of parameter `region`. Defaults to "us".
        :type region: type
        :param **apiArgs: Description of parameter `**apiArgs`.
        :type **apiArgs: type
        :return: Description of returned object.
        :rtype: type
        :raises ExceptionName: Why the exception is raised.

        """
        region = region.lower()
        if region not in self._regionmap:
            raise ZohoUnknownRegionException(region)
        self._org = organization_id
        self._endpoint = self.get_endpoint(region)
        self._oauth = f"https://accounts.zoho.{self._regionmap[region]}/oauth/v2"
        self._ratelimit = { 'limit': None, 'reset': None, 'remaining': 99999999 }
        self._api_keys = {
            'access_token': None,
            'client_id': None,
            'client_secret': None,
            'redirect_url': None,
            'refresh_token': None,
            'max_retries': 10,
            'retry_backoff_seconds': 0.5,
            'max_retry_after': 180,
            'min_calls_remaining': 1,
        }
        self.update_tokens(apiArgs)

    def auth_header(self):
        if self._api_keys.get('access_token') and self._api_keys['expires_at'] > datetime.datetime.now():
            return {'Authorization': f"Zoho-oauthtoken {self._api_keys['access_token']}"}
        if self._api_keys.get('refresh_token'):
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
                raise ZohoAPICallsExceeded()
        retries = self._api_keys['max_retries']
        while True:
            reqparams = {
                'headers': self.auth_header(),
                'files': files,
                'json': body,
            }
            rsp = requestFunc(url, **reqparams)
            if rsp.status_code == 429 and retries:  # Too Many Requests
                retries -= 1
                sleeptime = int(rsp.headers.get('retry-after', self._api_keys['retry_backoff_seconds']))
                if sleeptime <= self._api_keys['max_retry_after']:
                    sleep(sleeptime)
                else:
                    raise ZohoAPIThrottled()
            elif not rsp.ok:
                # TODO: raise more specific exceptions here
                raise ZohoException(f"Encountered #{rsp.status_code} error calling Zoho API")
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
                            sleep(sleeptime)
                        else:
                            raise ZohoAPIThrottled()
                else:
                    return rsp

    def delete(self, urlFragment):
        url = f"{self._endpoint}/{urlFragment}?organization={self._org}"
        rsp = self.do_request(requests.delete, url)
        return rsp.ok

    def get(self, urlFragment, queryString):
        url = f"{self._endpoint}/{urlFragment}?organization={self._org}&{queryString}"
        rsp = self.do_request(requests.get, url)
        if rsp.headers['content-type'].startswith("application/json"):
            data = rsp.json()
            if data['code'] == 0:
                return data
            raise ZohoException(f"zoho returned {data['code']}: {data['message']}")
        return {
            'content': rsp.content,
            'content_type': rsp.headers['content-type'],
        }

    def get_endpoint(self, region):
        # This MUST be overridden in subclasses for the APIs to work.
        # It's only here in the base class for testing
        return False

    def post(self, urlFragment, data=None, queryString="", files=None):
        url = f"{self._endpoint}/{urlFragment}?organization={self._org}&{queryString}"
        rsp = self.do_request(requests.post, url, data, files)
        if rsp.headers['content-type'].startswith("application/json"):
            data = rsp.json()
            if data['code'] == 0:
                return data
            raise ZohoException(f"zoho returned {data['code']}: {data['message']}")
        return {
            'content': rsp.content,
            'content_type': rsp.headers['content-type'],
        }

    def put(self, urlFragment, data, queryString):
        url = f"{self._endpoint}/{urlFragment}?organization={self._org}&{queryString}"
        rsp = self.do_request(requests.put, url, data)
        if rsp.headers['content-type'].startswith("application/json"):
            data = rsp.json()
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
        self._ratelimit['ResetAt'] = datetime.datetime.now()
        if self._ratelimit.get('reset'):
            self._ratelimit['ResetAt'] += datetime.timedelta(seconds=int(self._ratelimit['reset']))

    def update_tokens(self, apiArgs):
        self._api_keys.update(apiArgs)
        self._api_keys['expires_at'] = datetime.datetime.now() + datetime.timedelta(seconds=apiArgs.get('expires_in', 0) - 10)


class ZohoObjectBase:
    ID = property(lambda self: self._id)
    IsDeleted = property(lambda self: self._id is False)
    IsList = property(lambda self: isinstance(self._data, DottedList))
    IsLoaded = property(lambda self: self._data is not None)
    Number = property(lambda self: self._data[self._number_field] if self._id and self._data else None)

    def __init__(self, api, /, id=None, **searchParams):
        self._id = id
        self._api = api
        self._data = None
        self._nextpage = None
        if id or {k:v for k,v in searchParams.items() if isinstance(v, str)}:
            self._load(id=id, **searchParams)
        elif searchParams:
            self._data = DottedList()   # we aren't a list yet, but will be

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

    def _load(self, *, page=None, **searchParams):
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
                    self._data.extend(data.get(self._plural))
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

        :return: self (so you can chain) as updated by Zoho
        :rtype: ZohoObject
        """
        if not self._id:
            newData = self._api.post(self._url_fragment(), self._data.to_python(), self._query_string(**qParams))
            if newData:
                self._reload(newData)
            return self
        raise ZohoInvalidOpError("Create", self)


    def Delete(self):
        """ Delete this object from Zoho

        :return: self, but marked as deleted
        :rtype: ZohoObject
        """
        if self._id:
            if self._api.delete(self._url_fragment()):
                self._id = False
                self._data[self._id_field] = None
            return self
        raise ZohoInvalidOpError("Delete", self)

    def First(self):
        """ Get the first ZohoObject from the list.
        """
        if self._id:
            return self
        if not self._data:
            self._load()
        if self._data:
            return self.__class__(self._api, self._data[0][self._id_field])
        self._data = None
        return self

    def GetCustomField(self, key, *, listKey="custom_fields", default=None):
        if self._id:
            if self._data:
                for cf in self._data.get(listKey, []):
                    if key in [cf['label'], cf['placeholder']]:
                        return cf['value']
            return default
        raise ZohoInvalidOpError("GetCustomField", self)

    def GetRelated(self, targetType, key):
        if self._id and self._data:
            if isinstance(self._data.get(key), str):
                return targetType(self._data[key])
        raise ZohoInvalidOpError("GetRelated", self)

    def Iter(self, filterFunc=None, *, raw=False, **filter):
        """ Iterate over the list of ZohoObjects

        If called on a non-connected ("new") object, we get the list of ALL objects

        :param filterFunc: function which takes the item to test, returning True or False
        :type filter: callable
        :param raw: return the raw list data?
        :type raw: bool
        :param filter: fields/values to filter the list by
        :type filter: dict
        :return: iterable of ZohoObjects
        :rtype: iterable
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
                yield {'meta': item, 'object': targetType(item.get(idField))}
        else:
            raise ZohoInvalidOpError("MapRelatedList", self)

    def Update(self):
        if self._id and self._data:
            updated = diff(self._orig, self._data.to_python())
            if updated:
                for k in self._req_fields:
                    if self._data.get(k):
                        updated[k] = self._data[k]
                data = self._api.put(self._url_fragment(), updated, "")
                self._reload(data)
            return self
        raise ZohoInvalidOpError("Update", self)
