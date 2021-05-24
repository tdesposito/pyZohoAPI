# This file is part of pyZohoAPI, Copyright (C) Todd D. Esposito 2021.
# Distributed under the MIT License (see https://opensource.org/licenses/MIT).
import datetime

from ...exceptions import *

class WithBundle:
    def MakeBundle(self, qty, bundle_date=None, purchase_account_id=None, warehouse_id=None):
        """ Create a bundle for a CompositeItem

        :param qty: Number of bundles to make.
        :param bundle_date: Date of bundling, in "YYYY-MM-DD" format. Defaults to today.
        :param purchase_account_id: ID of the purchase account. Defaults to None.
        :param warehouse_id: ID of the warehouse to make the bundle in. Defaults to None.
        :return: Bundle ZohoObject
        :raises ZohoInvalidOpError: if `self` is new, a list, or not loaded.
        """
        if self.IsLoaded and self.ID:
            bundle = self._api.Bundle()
            bundle.date = bundle_date if bundle_date else datetime.datetime.today().strftime("%Y-%m-%d")
            bundle.composite_item_id = self.ID
            bundle.composite_item_name = self.name
            if self.get('sku'):
                bundle.composite_item_sku = self.get('sku')
            bundle.quantity_to_bundle = qty
            bundle.is_completed = True
            bundle.line_items = []
            for line in self.mapped_items:
                bundle_line = {
                    'item_id': line['item_id'],
                    'name': line['name'],
                    'unit': line['unit'],
                    'rate': line['purchase_rate'],
                    'quantity_consumed': line['quantity'],
                }
                if purchase_account_id:
                    bundle_line['account_id'] = purchase_account_id
                if warehouse_id:
                    bundle_line['warehouse_id'] = warehouse_id
                bundle.line_items.append(bundle_line)

            return bundle.Create()
        raise ZohoInvalidOpError('MakeBundle', self)
