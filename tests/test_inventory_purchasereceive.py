# This file is part of pyZohoAPI, Copyright (C) Todd D. Esposito 2021.
# Distributed under the MIT License (see http://opensource.org/licenses/MIT).

from pprint import pprint

from pyzohoapi.inventory import ZohoInventory
from pyzohoapi.exceptions import ZohoException

from private import testdata

z = ZohoInventory(testdata.orgid, testdata.region, **testdata.api)

def test_inventory_purchasereceive():
    o = z.PurchaseReceive(testdata.inventory.purchasereceive.purchasereceive_id)
    assert o.IsLoaded
    assert o.purchaseorder_number == testdata.inventory.purchasereceive.purchaseorder_number
