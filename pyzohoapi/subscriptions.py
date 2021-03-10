from .core import ZohoAPIBase
from .exceptions import ZohoException
from . import objecttypes

class ZohoSubscriptions(ZohoAPIBase):
    _scope = ZohoSubscriptions.fullaccess.all

    def get_endpoint(self, region):
        return f"https://inventory.zoho.{self._regionmap[region]}/api/v1"

    def AddOn(self, *args, **kwargs): return objecttypes.AddOn(self, *args, **kwargs)
    def Coupon(self, *args, **kwargs): return objecttypes.Coupon(self, *args, **kwargs)
    def CreditNote(self, *args, **kwargs): return objecttypes.CreditNote(self, *args, **kwargs)
    def Customer(self, *args, **kwargs): return objecttypes.Customer(self, *args, **kwargs)
    def HostedPage(self, *args, **kwargs): return objecttypes.HostedPage(self, *args, **kwargs)
    def Invoice(self, *args, **kwargs): return objecttypes.Invoice(self, *args, **kwargs)
    def Payment(self, *args, **kwargs): return objecttypes.Payment(self, *args, **kwargs)
    def Plan(self, *args, **kwargs): return objecttypes.Plan(self, *args, **kwargs)
    def Product(self, *args, **kwargs): return objecttypes.Product(self, *args, **kwargs)
    def Setting(self, *args, **kwargs): return objecttypes.Setting(self, *args, **kwargs)
    def Subcription(self, *args, **kwargs): return objecttypes.Subscription(self, *args, **kwargs)
    def WebHook(self, *args, **kwargs): return objecttypes.WebHook(self, *args, **kwargs)