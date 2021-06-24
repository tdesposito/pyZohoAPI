# Type Reference

```{include} /snippets/seealso-zoho-api.markdown
```
## Alphabetic
This is an alphabetic list of all the Zoho Object types we support, and the APIs
which include them.

We note which [additional methods](/objrefs/methods.md) each object type
includes, if any.

### Account
```{admonition} Available In
Books, Inventory
```

### Bill
```{admonition} Available In
Inventory
```
```{admonition} Additional methods
:class: tip

* [GetCustomField()](methods.md#getcustomfield)
* [SetCustomField()](methods.md#setcustomfield)
```

### Brand
```{admonition} Available In
Inventory
```

### Bundle
```{admonition} Available In
Inventory
```

### CreditNote
```{admonition} Available In
Inventory
```
```{admonition} Additional methods
:class: tip

* [GetCustomField()](methods.md#getcustomfield)
* [SetCustomField()](methods.md#setcustomfield)
```

### CompositeItem
```{admonition} Available In
Inventory
```
```{admonition} Additional methods
:class: tip

* [Activate()](methods.md#activate)
* [Deactivate()](methods.md#deactivate)
* [GetCustomField()](methods.md#getcustomfield)
* [MakeBundle()](methods.md#makebundle)
* [SetCustomField()](methods.md#setcustomfield)
```

### Contact
```{admonition} Available In
Inventory
```
```{admonition} Additional methods
:class: tip

* [Activate()](methods.md#activate)
* [Deactivate()](methods.md#deactivate)
* [GetCustomField()](methods.md#getcustomfield)
* [SetCustomField()](methods.md#setcustomfield)
* [UpdateBilling()](methods.md#updatebilling)
* [UpdateShipping()](methods.md#updateshipping)
```

### CustomerPayment
```{admonition} Available In
Inventory
```

### Currency
```{admonition} Available In
Inventory
```

### Document
```{admonition} Available In
Books, Inventory
```
Retrieving a List-of Document objects will get your the typical List-of. Getting
a particular Document (by ID, or iterating over the list) will get you object(s)
with two fields:
* `content` is the raw, binary version of the document;
* `content_type` is the MIME-type of the content;
```{warning}
The document content could be very large, and will be loaded into memory. Use
with care.
```

### Invoice
```{admonition} Available In
Books, Inventory
```

### Item
```{admonition} Available In
Books, Inventory
```
```{admonition} Additional methods
:class: tip

* [Activate()](methods.md#activate)
* [AddImage()](methods.md#addimage)
* [Deactivate()](methods.md#deactivate)
* [DeleteImage()](methods.md#deleteimage)
* [GetCustomField()](methods.md#getcustomfield)
* [SetCustomField()](methods.md#setcustomfield)
```
### ItemAdjustment
```{admonition} Available In
Inventory
```

### ItemGroup
```{admonition} Available In
Inventory
```
```{admonition} Additional methods
:class: tip

* [Activate()](methods.md#activate)
* [Deactivate()](methods.md#deactivate)
```

### Organization
```{admonition} Available In
Books, Inventory
```

### Package
```{admonition} Available In
Inventory
```

### PriceList
```{admonition} Available In
Inventory
```

### PurchaseOrder
```{admonition} Available In
Books, Inventory
```

### PurchaseReceive
```{admonition} Available In
Inventory
```

### RetainerInvoice
```{admonition} Available In
Books, Inventory
```

### SalesOrder
```{admonition} Available In
Books, Inventory
```
```{admonition} Additional methods
:class: tip

* [Confirm()](methods.md#confirm)
* [GetCustomField()](methods.md#getcustomfield)
* [SetCustomField()](methods.md#setcustomfield)
* [Void()](methods.md#void)
```

### SalesPerson
```{admonition} Available In
Books, Inventory
```
```{admonition} Additional methods
:class: note
You can only get the list of all Sales Persons from the API. No other operations
work.
```

### SalesReturn
```{admonition} Available In
Inventory
```

### ShipmentOrder
```{admonition} Available In
Books, Inventory
```

### Tax
```{admonition} Available In
Inventory
```

### TaxAuthority
```{admonition} Available In
Inventory (US Edition Only)
```

### TaxExemption
```{admonition} Available In
Inventory (US Edition Only)
```

### TaxGroup
```{admonition} Available In
Inventory (Non-US Edition Only)
```

### TransferOrder
```{admonition} Available In
Inventory
```

### User
```{admonition} Available In
Books, Inventory
```
```{admonition} Additional methods
:class: tip

* [Activate()](methods.md#activate)
* [Deactivate()](methods.md#deactivate)
* [GetCustomField()](methods.md#getcustomfield)
* [SetCustomField()](methods.md#setcustomfield)
```

### Warehouse
```{admonition} Available In
Inventory
```
```{warning}
Warehouse does not support Get-By-ID semantics. Always use `.Iter(raw=True)`
when walking the list of warehouses.

This also means **ANY** operation which returns or acts on an existing warehouse
is not currently supported.
```

## By Product

### Books
```{warning}
Books support is still under development.
```

### Checkout
```{include} ../snippets/todo-future-release.markdown
```

### Expense
```{include} ../snippets/todo-future-release.markdown
```

### Inventory
* [Account](#account)
* [Bundle](#bundle)
* [CompositeItem](#compositeitem)
* [Contact](#contact)
* ContactPerson (TODO)
* [CustomerPayment](#customerpayment)
* [Currency](#currency)
* [Document](#document)
* [Invoice](#invoice)
* [Item](#item)
* [ItemAdjustment](#itemadjustment)
* [ItemGroup](#itemgroup)
* [Organization](#organization)
* [Package](#package)
* [PriceList](#pricelist)
* [PurchaseOrder](#purchaseorder)
* [PurchaseReceive](#purchasereceive)
* [RetainerInvoice](#retainerinvoice)
* [SalesOrder](#salesorder)
* [SalesPerson](#salesperson)
* [SalesReturn](#salesreturn)
* [ShipmentOrder](#shipmentorder)
* [Tax](#tax)
* [TaxAuthority](#taxauthority)
* [TaxExemption](#taxexemption)
* [TaxGroup](#taxgroup)
* [TransferOrder](#transferorder)
* [User](#user)
* VendorCredit (TODO)
* [Warehouse](#warehouse)

### Invoice
```{include} ../snippets/todo-future-release.markdown
```

### Subscriptions
```{include} ../snippets/todo-future-release.markdown
```
