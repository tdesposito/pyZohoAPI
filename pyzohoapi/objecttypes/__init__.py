# This file is part of pyZohoAPI, Copyright (C) Todd D. Esposito 2021.
# Distributed under the MIT License (see https://opensource.org/licenses/MIT).

from ..core import ZohoObjectBase
from .mixins import *

def ZohoObjectFactory(name,
    urlPath=None, responseKey=None,
    idKey=None, numberKey=None, raw=False,
    mixins=[]):
    """ Factory function to create a Zoho Object type

    Unless overridden by the optional paremters, `name` is used to determine how
    Zoho API objects are accessed and parsed.

    * The URL used will be https:/{api-root}/{pluralized `name` -or- `urlPath`}
    * A list of objects is under the JSON key pluralized `name` -or- pluralized `responseKey`
    * A single object of objects is under the JSON key `name` -or- `responseKey`
    * The object ID is under the JSON key `name` _id -or- `idKey`
    * The object Number is under the JSON key `name` _number -or- `numberKey`

    :param name: object-class name; the basis of the API URL path unless overridden.
    :param urlPath: overrides th API URL path
    :param responseKey: overrides how the singular/plural response keys are formed.
    :param idKey: overrides the id field key.
    :param numberKey: overrides the number field key.
    :param raw: handle the response body as raw data rather than json for non-list responses
    :param mixins: list of object-type mixins. Defaults to [].
    :return: ZohoObject sub-class
    """
    return type(name, tuple([ZohoObjectBase] + mixins), {
        '__name__': name,
        '_type': urlPath if urlPath else f"{name.lower()}s",
        '_singular': responseKey if responseKey else name.lower(),
        '_plural': f"{responseKey}s" if responseKey else f"{name.lower()}s",
        '_id_field': idKey if idKey else f"{name.lower()}_id",
        '_number_field': numberKey if numberKey else f"{name.lower()}_number",
        '_is_raw': raw,
    })

Account = ZohoObjectFactory("ChartOfAccount", idKey="account_id")
Bill = ZohoObjectFactory("Bill", mixins=[HasCustomFields])
Bundle = ZohoObjectFactory("Bundle")
CompositeItem = ZohoObjectFactory("CompositeItem",
    responseKey="composite_item", idKey="composite_item_id",
    mixins=[HasActivate, HasBundle, HasCustomFields])
Contact = ZohoObjectFactory("Contact", mixins=[HasActivate, HasAddresses])
CreditNote = ZohoObjectFactory("CreditNode", mixins=[HasCustomFields])
CustomerPayment = ZohoObjectFactory("CustomerPayment",
    idKey="payment_id", numberKey="payment_number", mixins=[HasCustomFields])
Document = ZohoObjectFactory("Document", raw=True)
Invoice = ZohoObjectFactory("Invoice", mixins=[HasCustomFields])
Item = ZohoObjectFactory("Item", mixins=[HasActivate, HasCustomFields, HasImage])
ItemGroup = ZohoObjectFactory("ItemGroup", idKey="group_id",
    responseKey="group", mixins=[HasActivate])
Organization = ZohoObjectFactory("Organization")
Package = ZohoObjectFactory("Package", mixins=[HasCustomFields])
PurchaseOrder = ZohoObjectFactory("PurchaseOrder", mixins=[HasCustomFields])
SalesOrder = ZohoObjectFactory("SalesOrder",
    mixins=[HasConfirm, HasCustomFields, HasVoid])
SalesPerson = ZohoObjectFactory("SalesPerson")
ShipmentOrder = ZohoObjectFactory("ShipmentOrder",
    responseKey="shipment_order", idKey="shipment_id",
    numberKey="shipment_number", mixins=[HasCustomFields])
User = ZohoObjectFactory("User", mixins=[HasActivate, HasCustomFields])
