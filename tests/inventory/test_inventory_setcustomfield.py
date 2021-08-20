# This file is part of pyZohoAPI, Copyright (C) Todd D. Esposito 2021.
# Distributed under the MIT License (see http://opensource.org/licenses/MIT).

from pprint import pprint

from pyzohoapi.inventory import ZohoInventory
from pyzohoapi.exceptions import ZohoException

from private import testdata

z = ZohoInventory(testdata.orgid, testdata.region, **testdata.api)

def test_inventory_item_setcustomfield():
    temp = z.Item()
    for key, value in testdata.inventory.item.tempitem.items():
        temp.__setattr__(key, value)
    temp.Create()

    assert temp.GetCustomField(testdata.inventory.item.customfield.label) is None
    temp.SetCustomField(testdata.inventory.item.customfield.label, testdata.inventory.item.customfield.value).Update()
    assert temp.GetCustomField(testdata.inventory.item.customfield.label) == testdata.inventory.item.customfield.value

    # load a fresh copy, to be sure the DB is updated, not just our local copy
    fresh = z.Item(temp.ID)
    assert fresh.GetCustomField(testdata.inventory.item.customfield.placeholder) == testdata.inventory.item.customfield.value

    temp.Delete()
