# This file is part of pyZohoAPI, Copyright (C) Todd D. Esposito 2021.
# Distributed under the MIT License (see http://opensource.org/licenses/MIT).

from pprint import pprint

from pyzohoapi.inventory import ZohoInventory
from pyzohoapi.exceptions import ZohoException

from private import testdata

z = ZohoInventory(testdata.orgid, testdata.region, **testdata.api)

def test_core_first():
    # verify that First gets the first in the unfiltered list
    c = z.Currency().First()
    assert c.IsLoaded
    assert c.currency_code == testdata.core.first.first_currency_code

    # verify that First respects filtering
    c = z.Currency().First(currency_code=testdata.core.first.filtered_currency_code)
    assert c.IsLoaded
    assert c.currency_code == testdata.core.first.filtered_currency_code

    # verify that First returns "empty" on filter-failure
    c = z.Currency().First(currency_code=testdata.core.first.invalid_currency_code)
    assert not c.IsLoaded
