# Type-Specific Methods
These methods are added to objects which support the corresponding semantics.

Not every object has every one, or indeed any, of the below.

```{warning}
Due to how we implement the Zojo objects, calling one of these methods on an
object without support for it will raise a `KeyError` rather than the more
typical `AttributeError`. Please code appropriately.
```
```{include} /snippets/seealso-zoho-api.markdown
```

## Alphabetically
### `Activate()`
Makes the object "Active". True on success. Raises `ZohoInvalidOpError` if
called on a New or List-of object.
```{admonition} Applies To
:class: tip

* [CompositeItem](types.md#compositeitem)
* [Contact](types.md#contact)
* [Item](types.md#item)
* [ItemGroup](types.md#itemgroup)
* [User](types.md#user)
```

### `AddImage()`
Add an image to an object.
```{code-block} python
>>> imgname = "imagename.jpg"
>>> mimetype = "image/jpeg"
>>> with open(imgname, "rb") as image:
...   obj.AddImage(imgname, image.read(), mimetype)
```
```{admonition} Applies To
:class: tip

* [Item](types.md#item)
```

### `Confirm()`
Marks an object as "Confirmed". Returns True on success. Raises
`ZohoInvalidOpError` if called on a New or List-of object.
```{admonition} Applies To
:class: tip

* [SalesOrder](types.md#salesorder)
```

### `Deactivate()`
Makes the object "Inactive". True on success. Raises `ZohoInvalidOpError` if
called on a New or List-of object.
```{admonition} Applies To
:class: tip

* [CompositeItem](types.md#compositeitem)
* [Contact](types.md#contact)
* [Item](types.md#item)
* [ItemGroup](types.md#itemgroup)
* [User](types.md#user)
```

### `DeleteImage()`
Deletes the image associated with an object.
```{admonition} Applies To
:class: tip

* [Item](types.md#item)
```

### `Delivered()`
Marks an object as "Delivered". Returns True on success. Raises `ZohoInvalidOpError`
if called on a New or List-of object.
```{admonition} Applies To
:class: tip

* [ShipmentOrder](types.md#shipmentorder)
```

### `Draft()`
Marks an object as "Draft". Returns True on success. Raises `ZohoInvalidOpError`
if called on a New or List-of object.

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
```{admonition} Applies To
:class: tip

* [CompositeItem](types.md#compositeitem)
* [Item](types.md#item)
* [SalesOrder](types.md#salesorder)
```

### `MakeBundle()`
Bundles a CompositeItem n-Many times. Provide the number of bundles to make as the first parameter, and optionally these keyword parameters:
  * `bundle_date` (string): the date, in "YYYY-MM-DD" format, for the bundles. Defaults to today.
  * `purchase_account_id` (string): the ID of the corresponding purchase account.
  * `warehouse_id` (string): the ID of the corresponding warehouse (required if warehouses are enabled).
```{admonition} Applies To
:class: tip

* [CompositeItem](types.md#compositeitem)
```

```{code-block} python
>>> composite.MakeBundle(10, purchase_account_id="9878765432165432109")
Bundle #9876543210987654321
```

### `SetCustomField()`
**_Updated in v0.6.0_**: Moved out of Common Methods

**_New in v0.5.0_**

Sets the value of a custom field in the object, and returns the object. You pass
either the custom field `placeholder` or `label` as the first parameter, and the
new value as the second. `SetCustomField()` returns the object, so it can be
chained.

If the custom field doesn't exist in the object, we'll try to add it. However,
sometimes the Zoho API wants `placeholder` and sometimes it wants `label`. so
you have to provide the correct one.
```{admonition} Applies To
:class: tip

* [CompositeItem](types.md#compositeitem)
* [Item](types.md#item)
* [SalesOrder](types.md#salesorder)
```

### `UpdateBilling()`
Updates the related Billing Address of the object.
```{code-block} python
>>> contact.billing_address.address = "123 New Street"
>>> contact.UpdateBilling()
Contact #9876543210987654321
```
```{admonition} Applies To
:class: tip

* [Contact](types.md#contact)
```

### `UpdateShipping()`
Updates the related Shipping Address of the object.
```{code-block} python
>>> contact.shipping_address.address = "123 New Street"
>>> contact.UpdateShipping()
Contact #9876543210987654321
```
```{admonition} Applies To
:class: tip

* [Contact](types.md#contact)
```

### `Void()`
Marks an object as "Void". Returns True on success. Raises `ZohoInvalidOpError`
if called on a New or List-of object.
```{admonition} Applies To
:class: tip

* [SalesOrder](types.md#salesorder)
```
