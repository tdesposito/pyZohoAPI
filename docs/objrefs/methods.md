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

### `AddImage()`
Add an image to an object.
```{code-block} python
>>> imgname = "imagename.jpg"
>>> mimetype = "image/jpeg"
>>> with open(imgname, "rb") as image:
...   obj.AddImage(imgname, image.read(), mimetype)
```

### `Confirm()`
Marks an object as "Confirmed". Returns True on success. Raises
`ZohoInvalidOpError` if called on a New or List-of object.

### `Deactivate()`
Makes the object "Inactive". True on success. Raises `ZohoInvalidOpError` if
called on a New or List-of object.

### `DeleteImage()`
Deletes the image associated with an object.

### `Draft()`
Marks an object as "Draft". Returns True on success. Raises `ZohoInvalidOpError`
if called on a New or List-of object.

### `MakeBundle()`
Bundles a CompositeItem n-Many times. Provide the number of bundles to make as the first parameter, and optionally these keyword parameters:
  * `bundle_date` (string): the date, in "YYYY-MM-DD" format, for the bundles. Defaults to today.
  * `purchase_account_id` (string): the ID of the corresponding purchase account.
  * `warehouse_id` (string): the ID of the corresponding warehouse (required if warehouses are enabled).

```{code-block} python
>>> composite.MakeBundle(10, purchase_account_id="9878765432165432109")
Bundle #9876543210987654321
```

### `UpdateBilling()`
Updates the related Billing Address of the object.
```{code-block} python
>>> contact.billing_address.address = "123 New Street"
>>> contact.UpdateBilling()
Contact #9876543210987654321
```

### `UpdateShipping()`
Updates the related Shipping Address of the object.
```{code-block} python
>>> contact.shipping_address.address = "123 New Street"
>>> contact.UpdateShipping()
Contact #9876543210987654321
```

### `Void()`
Marks an object as "Void". Returns True on success. Raises `ZohoInvalidOpError`
if called on a New or List-of object.
