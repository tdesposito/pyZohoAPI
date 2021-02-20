# Type Reference

```{include} /snippets/seealso-zoho-api.markdown
```
## Alphabetic
This is an alphabetic of all the Zoho Object types we support, and the APIs
which include them.

We note which [additional methods](/objrefs/methods.md) each object type
includes, if any.
### Account
```{admonition} Chart-Of-Accounts
Books, Inventory
```

### Bundle
```{admonition} Bundle
Inventory
```

### CompositeItem
```{admonition} Composite Items
Inventory
```
```{admonition} Additional methods
:class: tip

* Activate
* Deactivate
```

### Contact
```{admonition} Contacts
Inventory
```
```{admonition} Additional methods
:class: tip

* Activate
* Deactivate
* UpdateBilling
* UpdateShipping
```

### CustomerPayment
```{admonition} Customer Payments
Inventory
```

### Document
```{admonition} Documents
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
```{admonition} Invoices
Books, Inventory
```

### Item
```{admonition} Items
Books, Inventory
```
```{admonition} Additional methods
:class: tip

* Activate
* AddImage
* Deactivate
* DeleteImage
```

### ItemGroup
```{admonition} Item Groups
Inventory
```
```{admonition} Additional methods
:class: tip

* Activate
* Deactivate
```

### Organization
```{admonition} Organizations
Books, Inventory
```

### Package
```{admonition} Packages
Inventory
```

### PurchaseOrder
```{admonition} Purchase Orders
Books, Inventory
```

### SalesOrder
```{admonition} Sales Orders
Books, Inventory
```

### ShipmentOrder
```{admonition} Shipment Orders
Books, Inventory
```

### User
```{admonition} Users
Books, Inventory
```
```{admonition} Additional methods
:class: tip

* Activate
* Deactivate
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
* [CustomerPayment](#customerpayment)
* [Document](#document)
* [Invoice](#invoice)
* [Item](#item)
* [ItemGroup](#itemgroup)
* [Organization](#organization)
* [Package](#package)
* [PurchaseOrder](#purchaseorder)
* [SalesOrder](#salesorder)
* [ShipmentOrder](#shipmentorder)
* [User](#user)

### Invoice
```{include} ../snippets/todo-future-release.markdown
```

### Subscriptions
```{include} ../snippets/todo-future-release.markdown
```
