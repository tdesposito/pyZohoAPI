# Quick Start

## Installation
```{include} ../README.md
:start-after: <!-- start installation -->
:end-before: <!-- end installation -->
```
## Basic Usage
```{include} ../README.md
:start-after: <!-- start basic-usage -->
:end-before: <!-- end basic-usage -->
```

## API Objects
All operations are, one way or another, performed via one of the several
product-specific "API" objects, each named for the API they target. In the
example above, we are using the "Inventory" API via the _ZohoInventory_ object.

Each API object follows this pattern:
```
api = ZohoProduct(organization_id, region="us", **apiArgs)
```
where _ZohoProduct_ is one of _ZohoBooks, ZohoCheckout, ZohoExpense,
ZohoInventory, ZohoInvoice, and ZohoSubscriptions_.

```{note}
As of this release, we only include support for _Inventory_.
```
`region` should be either the Top-Level Domain name of the region you're in, or
the region's "friendly" name (case insensitive), one of _Australia, Europe,
India, US_.

Generally, provide client_id, client_secret, refresh_token and redirect_url as
keyword arguments.

```{note}
You won't need redirect_url for Self-Client or Non-Browser Client access.
```
```{warning}
Client ID and Secrets are just that: SECRET. Please don't include them directly
in any code you might share.
```
```{seealso}
Zoho uses OAuth procedures to provide your Access Tokens. Please see  [Zoho's
API Documentation on OAuth](https://www.zoho.com/inventory/api/v1/#oauth) for
details.
```

## Zoho Objects
You access Zoho Objects via the API Object. Let's assume you have an
_inventory_ object defined as:
```{code-block} python
inventory = ZohoInventory(...)
```
Now you can get various Zoho objects by using their type name, thus:
```{code-block} python
user = inventory.User(...)
item = inventory.Item(...)
composite = inventory.CompositeItem(...)
```

### Object Properties
We surface a small number of properties, to wit:
| Property  | Purpose |
| :--- | ---: |
| ID        | The Zoho id number of the underlying object.  |
| IsDeleted | True if the object was deleted from Zoho.     |
| IsList    | True if the object is a list of Zoho objects  |
| IsLoaded  | True if we've fetched the corresponding object or list from Zoho |
| Number    | The Zoho document number of the underlying object |

### Get an Existing Object
If you know the object ID:
```{code-block} python
customer = inventory.Contact(id)
```

If you know some other unique identifier, take the first (only) object from a
search for that identifier.
```{code-block} python
customer = inventory.Contact(email="test@example.com").First()
```

### Create a new Object
Instantiate a new object, set its fields, and Create() it. If it now has an ID,
it was created.
```{code-block} python
invoice = inventory.Invoice()
invoice.customer_id = customer.ID
... # more fields should be set here.
invoice.Create()
if invoice.ID:
  print("Invoice created!")
```

### Update an Existing Object
Given an object, change or add whichever fields you want, then Update() it.
```{code-block} python
customer.first_name = "Ford"
customer.last_name = "Prefect"
customer.Update()
```

### Delete an Existing Object
Deleting an object in Zoho doesn't zap the data in the Python object, so it's
available, if needed.
```{code-block} python
if invoice.Delete().IsDeleted:
  print(f"Deleted invoice {invoice.Number}")
```

### Get a list of Objects
You can iterate over EVERY object of a particular type.
```{code-block} python
for user in inventory.User():
  print(user.name)
```
```{warning}
Use this with form with care. The above example, User, is likely not going to
result in a huge list, but if you were to iterate over every, say, Invoice or
Item in your organization, you could very well run yourself out of API calls.
```

You can search and filter lists of objects.
```{code-block} python
items = inventory.Item(category_id="9876543210987654321")
for item in items:
  print(item.name)
for item in items.Iter(lambda item: item.sku.startswith('S123'))
  print(item.name)
```
The first loop gathers all Item objects which match the criteria specified. The
second loop walks **the same list as the first**, but only prints those which
pass the filter function.

```{warning}
The following is a Bad Idea, because it will request EVERY Item in your
inventory prior to filtering.
  ```{code-block} python
  items = inventory.Item()
  for item in items.Iter(lambda item: item.sku.startswith('S123'))
    print(item.name)
  ```
```
