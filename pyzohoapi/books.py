# This file is part of pyZohoAPI, Copyright (C) Todd D. Esposito 2021.
# Distributed under the MIT License (see http://opensource.org/licenses/MIT).

from .core import ZohoAPIBase
from .exceptions import ZohoException
from . import objecttypes

class ZohoBooks(ZohoAPIBase):
    _scope = "ZohoBooks.FullAccess.all"

    def get_endpoint(self, region):
        return f"https://books.zoho.{self._regionmap[region]}/api/v3"

    def Account(self, *args, **kwargs): return objecttypes.Account(self, *args, **kwargs)
    def CompositeItem(self, *args, **kwargs): return objecttypes.CompositeItem(self, *args, **kwargs)
    def Contact(self, *args, **kwargs): return objecttypes.Contact(self, *args, **kwargs)
    def CustomerPayment(self, *args, **kwargs): return objecttypes.CustomerPayment(self, *args, **kwargs)
    def Document(self, *args, **kwargs): return objecttypes.Document(self, *args, **kwargs)
    def Invoice(self, *args, **kwargs): return objecttypes.Invoice(self, *args, **kwargs)
    def Item(self, *args, **kwargs): return objecttypes.Item(self, *args, **kwargs)
    def ItemGroup(self, *args, **kwargs): return objecttypes.ItemGroup(self, *args, **kwargs)
    def Organization(self, *args, **kwargs): return objecttypes.Organization(self, *args, **kwargs)
    def PurchaseOrder(self, *args, **kwargs): return objecttypes.PurchaseOrder(self, *args, **kwargs)
    def SalesOrder(self, *args, **kwargs): return objecttypes.SalesOrder(self, *args, **kwargs)
    def SalesPerson(self, *args, **kwargs): return objecttypes.SalesPerson(self, *args, **kwargs)
    def User(self, *args, **kwargs): return objecttypes.User(self, *args, **kwargs)
