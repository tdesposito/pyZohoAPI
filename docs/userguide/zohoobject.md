# Zoho Objects

The Python object which represents a Zoho object can also represent a list of
Zoho objects, depending on the parameters passed during instantiation.

If you pass in the Zoho ID of the object, the Python object will map to that
particular Zoho object. In all other cases, the Python object is a List-of those
Zoho objects. Except if you pass NO parameters, then you get a "New" object. If
you then iterate on it, it becomes a list. Strange but true.

## Common Methods
These are the methods available in EVERY Zoho object. Not every method makes
sense in every context, and in those cases the method will generally No-op.

Many methods return *self*, so they can be chained.

As the header of this section suggests, there are also object-specific methods.
These are documented in the [Object Type Reference](/objrefs/index.md) section.

### Accessor/Constructor
To get an object of a particular type, you do something of the form:
```{code-block} python
>>> obj = api.ObjectType()
>>> print(obj)
New ObjectType
```

If you know the Zoho ID of the object you want, then:
```{code-block} python
>>> obj = api.ObjectType(id)
>>> print(obj)
ObjectType #9876543210987654321
```

Or you can specify API search criteria as key/value parameters:
```{code-block} python
>>> obj = api.ObjectType(search_criteria="9876543210987654321")
>>> print(obj)
List of ObjectType objects
```
```{note}
The above are (I hope clearly) just examples and are not directly usable.
There's no Zoho object called (as of this writing) "ObjectType".
```

### `Create()`
```{code-block} python
item = inventory.Item()
item.name = "Test Item"
item.rate = 42.00
item.Create()
if item.ID:
  print(item.available_stock)
```
There is no checking to ensure all required fields are set, nor that any of the
values make sense. If the object was created in Zoho, *self* gets an **ID** and
is updated with all default fields Zoho provided.

Calling `Create()` on a not-New object is a No-Op.

### `Delete()`
```{code-block} python
>>> item = inventory.Item(id)
>>> item.ID
9876543210987654321
>>> item.Delete().IsDeleted
True
>>> item.ID
False
>>> item.item_id
None
```
After deleting the object from Zoho, all the field data is still available in
the Python object, so in theory you could re-create the object by calling
`Create()`, or modify it and then re-create. YMMV. Of course, you'll get a
new **ID** in that case.

Calling `Delete()` on a List-of or New object is a No-Op.

### `First()`
```{code-block} python
user = inventory.User(email="test@example.com").First()
if user.IsLoaded:
  print("Loaded the user")
```
`First()` returns the first object found by a search; if called on a new or
mapped object, it returns *self*, so it's safe to use anywhere. Useful if you
know your search will only return one result.

### `GetCustomField()`
Returns the value of a Custom Field. Let's say you have a Custom Field on your
Items labeled "Bin Location" and named "cf_bin_location" (the Zoho field
`placeholder` name). Then you can:
```{code-block} python
>>> item.GetCustomField('cf_bin_location')
A234
>>> item.GetCustomField('Bin Location')
A234
```
If the Custom Field isn't part of the object, `GetCustomField()` returns None.
You can alter that behavior:
```{code-block} python
>>> item.GetCustomField('Invalid Label')
None
>>> item.GetCustomField('Invalid Label', default="Sup?")
'Sup?'
```
If the Custom Field list of the object isn't "custom_fields", or there's more
than one such list:
```{code-block} python
>>> item.GetCustomField('cf_bin_location', listkey='item_custom_fields')
A234
```

### `GetRelated()`
For object types which includes references to other object types,
`GetRelated()` will return that object:
```{code-block} python
>>> so = inventory.SalesOrder(id)
>>> contact = so.GetRelated(inventory.Contact, 'customer_id')
>>> contact.company_name
Acme International
```
`GetRelated()` is a more convenient and safe version of:
```{code-block} python
>>> so = inventory.SalesOrder(id)
>>> contact = inventory.Contact(so.customer_id)
>>> contact.company_name
Acme International
```

### `Iter()` and `__iter__()`
We handle pagination of List-of objects transparently, so you can treat List-of
objects as iterables:
```{code-block} python
for invoice in inventory.Invoice(date="2021-01-01", status="paid"):
  print(invoice.Number)
```
This has some potential drawbacks.

If your search criteria is too broad, the list could be much longer than you
really need, and EVERY object which matches your criteria will be individually
retrieved, costing you ***lots*** of API calls.

If you only need values from fields which are already in the search results,
and you don't need to manipulate each individual object, use `Iter()`
with the `raw` flag:
```{code-block} python
paid_today = inventory.Invoice(date="2021-01-01", status="paid")
for invoice in paid_today.Iter(raw=True):
  print(invoice.invoice_number)
```

```{note}
In the above example, we used the Zoho field name `invoice_number` rather
than the object property `Number` because **we didn't retrieve an object**. Here
`invoice` is a dictionary which supports using '.' in addition to '[]' semantics
for getting values.
```

You can also filter the list using `Iter()`. The caveat is that the field(s)
you're filtering on must exist in the search results:
```{code-block} python
paid_today = inventory.Invoice(date="2021-01-01", status="paid")
for invoice in paid_today.Iter(currency_code="USD", due_date="2021-02-28"):
  print(invoice.Number)
```

If you need a more complex filter, pass a function as the first parameter:
```{code-block} python
paid_today = inventory.Invoice(date="2021-01-01", status="paid")
for invoice in paid_today.Iter(lambda inv: inv.total > 1000.00):
  print(invoice.Number)
```

### `IterRelatedList()`
For objects which include one or more lists of references to other object types,
you can get each of those objects:
```{code-block} python
for item in so.IterRelatedList(inventory.Item, 'line_items', 'item_id'):
  print(item.name)
```

### `Update()`
Changes you make to the fields in an existing Zoho object are pushed into Zoho
by calling `Update()`.
```{code-block} python
salesorder.line_items.append({'item_id':"9876543210987654321", 'quantity': 2})
salesorder.shipping_charges += 12.50
salesorder.Update()
```

## Object Properties
### `ID`
Each Zoho object type has a different "id" field, but they are mapped to the
`ID` property of the corresponding Python object. For example:
```{code-block} python
>>> customer = inventory.Contact(id)
>>> customer.ID == customer.contact_id
True

>>> item = inventory.Item(id)
>>> item.ID == item.item_id
True
```

### `Number`
Some, but not all, Zoho object types have a "number" field. These are exposed
via the `Number` property. If the underlying object doesn't have a "number"
field, using the `Number` property will raise a `KeyError`.
```{code-block} python
>>> invoice = inventory.Invoice(id)
>>> invoice.Number
INV-09472

>>> item = inventory.Item(id)
>>> item.Number
...(snip)...
KeyError: 'item_number'
```

### `IsDeleted`
*True* if the object has been deleted from Zoho. The data contained within the
object is still available, except the object's native \*\_id field, which will
be *None*. The `ID` property will be *False*.

### `IsList`
*True* if the object is a List-of Zoho objects.
```{code-block} python
so_list = inventory.SalesOrder(customer_id=...)
if so_list.IsList:
  doSomething(so_list)
```

### `IsLoaded`
*True* if we've loaded ANY data from Zoho. This is helpful for testing if an
object was available in Zoho.
```{code-block} python
so = inventory.SalesOrder(id)
if so.IsLoaded:
  doSomething(so)
```
