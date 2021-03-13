# This file is part of pyZohoAPI, Copyright (C) Todd D. Esposito 2021.
# Distributed under the MIT License (see https://opensource.org/licenses/MIT).

from ..core import ZohoObjectBase
from .mixins import *

def ZohoObjectFactory(name, nameform=None, idform=None, raw=False, required=[], mixins=[]):
    """ Factory function to create a Zoho Object type

    :param name: object-class name, the basis of the API url
    :param nameform: override how the singular/plural entry keys are formed.
    :param idform: override how the id and number fields are formed.
    :param raw: handle the response body as raw data rather than json for non-list responses
    :param required: list of required-to-update fields. Defaults to [].
    :param mixins: list of object-type mixins. Defaults to [].
    :return: ZohoObject sub-class
    """
    return type(name, tuple([ZohoObjectBase] + mixins), {
        '__name__': name,
        '_type': f"{name.lower()}s",
        '_singular': nameform if nameform else name.lower(),
        '_plural': f"{nameform}s" if nameform else f"{name.lower()}s",
        '_id_field': f"{idform}_id" if idform else f"{name.lower()}_id",
        '_number_field': f"{idform}_number" if idform else f"{name.lower()}_number",
        '_is_raw': raw,
        '_req_fields': required,
    })

Account = ZohoObjectFactory("ChartOfAccount", idform="account")
Bundle = ZohoObjectFactory("Bundle")
CompositeItem = ZohoObjectFactory("CompositeItem", nameform="composite_item", idform="composite_item", mixins=[WithActivate])
Contact = ZohoObjectFactory("Contact", mixins=[WithActivate, WithAddresses])
CustomerPayment = ZohoObjectFactory("CustomerPayment", idform="payment")
Document = ZohoObjectFactory("Document", raw=True)
Invoice = ZohoObjectFactory("Invoice")
Item = ZohoObjectFactory("Item", mixins=[WithActivate, WithImage])
ItemGroup = ZohoObjectFactory("ItemGroup", idform="group", nameform="group", mixins=[WithActivate])
Organization = ZohoObjectFactory("Organization")
Package = ZohoObjectFactory("Package")
PurchaseOrder = ZohoObjectFactory("PurchaseOrder")
SalesOrder = ZohoObjectFactory("SalesOrder", mixins=[WithConfirm, WithVoid])
ShipmentOrder = ZohoObjectFactory("ShipmentOrder", idform="shipment")
User = ZohoObjectFactory("User", mixins=[WithActivate])
