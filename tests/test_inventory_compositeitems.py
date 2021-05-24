# This file is part of pyZohoAPI, Copyright (C) Todd D. Esposito 2021.
# Distributed under the MIT License (see http://opensource.org/licenses/MIT).

from pprint import pprint

from pyzohoapi.inventory import ZohoInventory
from pyzohoapi.exceptions import ZohoException

from private import testdata

z = ZohoInventory(testdata.orgid, testdata.region, **testdata.api)

def test_composite_bundle():
    composite = z.CompositeItem(testdata.inventory.composite.composite_item_id)
    assert composite.IsLoaded
    bundle = composite.MakeBundle(2,
        purchase_account_id=testdata.inventory.composite.purchase_account_id,
        warehouse_id=testdata.inventory.composite.warehouse_id
        )
    assert bundle.ID
