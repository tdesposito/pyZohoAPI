# Type-Specific Methods
These methods are added to objects which support the corresponding semantics.

Not every object has every one, or indeed any, of the below. Calling one of
these methods on an object without support for it will raise a `KeyError`.

```{include} /snippets/seealso-zoho-api.markdown
```

## `Activate()`
Makes the object "Active".

## `AddImage()`
Add an image to an object.
```{code-block} python
>>> imgname = "imagename.jpg"
>>> mimetype = "image/jpeg"
>>> with open(imgname, "rb") as image:
...   obj.AddImage(imgname, image.read(), mimetype)
```

## `Confirm()`
Marks an object as "Confirmed".

## `Deactivate()`
Makes the object "Inactive".

## `DeleteImage()`
Deletes the image associated with an object.

## `Draft()`
Marks an object as "Draft".

## `Void()`
Marks an object as "Void".
