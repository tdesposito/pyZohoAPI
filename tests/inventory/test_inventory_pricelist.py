# This file is part of pyZohoAPI, Copyright (C) Todd D. Esposito 2021.
# Distributed under the MIT License (see http://opensource.org/licenses/MIT).

from pprint import pprint

from pyzohoapi.inventory import ZohoInventory
from pyzohoapi.exceptions import ZohoException

from private import testdata

z = ZohoInventory(testdata.orgid, testdata.region, **testdata.api)

def test_inventory_pricelist():
    print()
    for o in z.PriceList().Iter(raw=True):
        print(o.name)
