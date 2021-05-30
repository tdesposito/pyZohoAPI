# Type Reference

```{include} /snippets/seealso-zoho-api.markdown
```
## Alphabetic
This is an alphabetic of all the Zoho Object types we support, and the APIs
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

### PurchaseOrder
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

### ShipmentOrder
```{admonition} Available In
Books, Inventory
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
* ContactPerson
* [CustomerPayment](#customerpayment)
* [Currency](#currency)
* [Document](#document)
* [Invoice](#invoice)
* [Item](#item)
* [ItemAdjustment](#itemadjustment)
* [ItemGroup](#itemgroup)
* [Organization](#organization)
* [Package](#package)
* PriceList
* [PurchaseOrder](#purchaseorder)
* PurchaseReceive
* RetainerInvoice
* [SalesOrder](#salesorder)
* [SalesPerson](#salesperson)
* SalesReturn
* [ShipmentOrder](#shipmentorder)
* Tax
* [TransferOrder](#transferorder)
* [User](#user)
* VendorCredit
* Warehouse

### Invoice
```{include} ../snippets/todo-future-release.markdown
```

### Subscriptions
```{include} ../snippets/todo-future-release.markdown
```
