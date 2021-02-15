# This file is part of pyZohoAPI, Copyright (C) Todd D. Esposito 2021.
# Distributed under the MIT License (see http://opensource.org/licenses/MIT).

import copy

import pytest

from pyzohoapi import __version__
from pyzohoapi.core import ZohoAPIBase
from pyzohoapi.exceptions import *

from private import testdata

def test_bad_region():
    with pytest.raises(ZohoUnknownRegionException):
        z = ZohoAPIBase(testdata['orgid'], "really-bad-region-name", **testdata['api'])

def test_expired_access_token():
    tokens = copy.copy(testdata['api'])
    del tokens['refresh_token']
    del tokens['client_id']
    del tokens['client_secret']
    z = ZohoAPIBase(testdata['orgid'], testdata['region'], **tokens)
    with pytest.raises(ZohoInsufficentAuthKeys):
        z.auth_header()

def test_refresh_access_token():
    z = ZohoAPIBase(testdata['orgid'], testdata['region'], **testdata['api'])
    new_token = z.auth_header()
    assert z._api_keys['expires_in'] >= 0
