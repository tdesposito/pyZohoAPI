# This file is part of pyZohoAPI, Copyright (C) Todd D. Esposito 2021.
# Distributed under the MIT License (see http://opensource.org/licenses/MIT).

import datetime
from pprint import pprint

from pyzohoapi.inventory import ZohoInventory
from pyzohoapi.exceptions import ZohoException

from private import testdata

z = ZohoInventory(testdata.orgid, testdata.region, **testdata.api)

def test_inventory_itemadjustments():
    # create a test item
    temp = z.Item()
    for key, value in testdata.inventory.item.tempitem.items():
        temp.__setattr__(key, value)
    temp.Create()

    try:
        # assert temp.available_stock == 0
        adj = z.ItemAdjustment()
        adj.date = datetime.datetime.today().strftime("%Y-%m-%d")
        for key, value in testdata.inventory.item.adjustment.items():
            adj.__setattr__(key, value)
        adj.line_items = [{
            'item_id': temp.ID,
            'quantity_adjusted': 1,
            'warehouse_id': testdata.inventory.warehouse_id
        }]
        adj.Create()

        temp2 = z.Item(temp.ID)
        assert temp2.available_stock == 1

        adj.Delete()
    except ZohoException as e:
        raise e
    finally:
        temp.Delete()
