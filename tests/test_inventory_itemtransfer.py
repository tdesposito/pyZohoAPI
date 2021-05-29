# This file is part of pyZohoAPI, Copyright (C) Todd D. Esposito 2021.
# Distributed under the MIT License (see http://opensource.org/licenses/MIT).

import datetime
from pprint import pprint

from pyzohoapi.inventory import ZohoInventory
from pyzohoapi.exceptions import ZohoException

from private import testdata

z = ZohoInventory(testdata.orgid, testdata.region, **testdata.api)

def test_inventory_transferorder():
    def qty_in_warehouse(item, warehouse_id):
        for wh in item.warehouses:
            if wh.warehouse_id == warehouse_id:
                return wh.warehouse_stock_on_hand
        return None

    temp = z.Item()
    for key, value in testdata.inventory.item.tempitem.items():
        temp.__setattr__(key, value)
    temp.Create()
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

    temp_reloaded = z.Item(temp.ID)
    assert qty_in_warehouse(temp_reloaded, testdata.inventory.warehouse_id) == 1
    assert qty_in_warehouse(temp_reloaded, testdata.inventory.aux_warehouse_id) == 0

    try:
        xfer = z.TransferOrder()
        xfer.date = datetime.datetime.today().strftime("%Y-%m-%d")
        xfer.from_warehouse_id = testdata.inventory.warehouse_id
        xfer.to_warehouse_id =  testdata.inventory.aux_warehouse_id
        xfer.is_intransit_code = False
        xfer.line_items = [{
            'item_id': temp.ID,
            'name': temp.name,
            'quantity_transfer': 1,
        }]
        xfer.Create()

        temp2 = z.Item(temp.ID)
        assert qty_in_warehouse(temp2, testdata.inventory.warehouse_id) == 0
        assert qty_in_warehouse(temp2, testdata.inventory.aux_warehouse_id) == 1

        xfer.Delete()
    except ZohoException as e:
        raise e
    finally:
        adj.Delete()
        temp.Delete()
