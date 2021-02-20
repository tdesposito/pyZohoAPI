# User's Guide

## Short Version

Create an API Object for the product(s) you want to access:
```{code-block} python
from pyzohoapi import *
from my_private_data import org_id, my_api_tokens_dict

inventory = ZohoInventory(org_id, "US", **my_api_tokens_dict)
```

Find existing things in Zoho:
```{code-block} python
customer = inventory.Contact(email="customer@example.com").First()
items = inventory.Item(search_text="product type")
```

Then make a new thing in Zoho:
```{code-block} python
invoice = inventory.Invoice()
invoice.customer_id = customer.ID
invoice.line_items = []
for item in items:
  invoice.line_items.append({
      'item_id': item.ID,
      'quantity': 1,
    })
invoice.Create()
if invoice.ID:
  print(f"Created Invoice {invoice.Number}")
```

Then do a thing with a thing in Zoho:
```{code-block} python
invoice.Approve()
```

## A Note on PEP8-Compliance
Yes, I know, my method/property names aren't PEP8-compliant. This is
intentional.

Because each Zoho object field is exposed as an attribute of the corresponding
Python object, and those are (1) lower_case_with_underscore and (2) could be the
same as one of my function names and (3) are subject to add/change/delete by
Zoho, I've decided to CamelCase my method and property names, to avoid
potential collision with any field name Zoho has or will expose in their
JSON responses.

I thought about changing the mapping from Zoho's lower_case_with_underscore to
CamelCase. That seems like more work than is needed, since the interface surface
of the Python objects is much smaller than the interface surface of the Zoho
objects.

On the brighter side, the internals are PEP8ie.

## Long Version
```{toctree}
apiobject
zohoobject
exceptions
```
