# Modifying The Code

## Repository Organization

The Repository has four sub-directories of note:

* `docs` - Contains the project documentation (you know, this)
* `pyzohoapi` - Contains the module code
* `tests` - Contains the unit and functional tests
* `tools` - Contains [tools to help in development](setup.md#helpful-dev-and-debug-tools)
    * `interactive-test-server.py` is a simple web interface for interrogating the Zoho APIs
    * `test-shell.py` starts up a python REPL shell with the API Objects preloaded

## Code Style

Generally, we adhere to the [PEP8 Code
Style](https://www.python.org/dev/peps/pep-0008/). However, as noted elsewhere
in these docs, our public interface (properties and methods) for "ZohoObjects"
use CamelCase rather than underscore_separated_words, to avoid possible conflict
with Zoho-surfaced object fields. This should only apply to ZohoObjects; all
others should follow PEP8.

In short:
* Indention is 4 spaces, not tabs
* method_names_look_like_this _except for in ZohoObject classes_
* ClassNamesLookLikeThis

## Classes
_ZohoObject_ classes represent particular objects exposed by the API.

_ZohoAPI_ classes connect to particular API endpoints.

## Adding new ZohoObject Classes
We'll use [Zoho Inventory API](https://www.zoho.com/inventory/api/v1/) as an
example in this section.

```{note}
Unfortunately, the official Zoho API Docs aren't always accurate. When in doubt,
use any of the various API client tools available to test the API directly. See
[our interactive tools](setup.md#helpful-dev-and-debug-tools).
```

### Examine the API Request and Response
Let's consider Zoho **Composite Items**:

We see that to retrieve a list of **Composite Items**, we call:

`get /compositeitems`

The JSON we get back looks like:
```{code-block} json
:emphasize-lines: 4, 6
{
    "code": 0,
    "message": "success",
    "composite_items": [
        {
            "composite_item_id": "9999999000001049029",
```

If we retrive a particular **Composite Item** with:

`get /compositeitems/9999999000001049029`

we'll get:
```{code-block} json
:emphasize-lines: 4, 5
{
    "code": 0,
    "message": "success",
    "composite_item": {
        "composite_item_id": "9999999000001049029",
```
So we see that:
* The object type (as defined by Zoho) is "Composite Items"
* The Python class name should be **CompositeItem** (singular)
* The URL fragment is `compositeitems` (plural)
* The "list of **Composite Items**" key is `composite_items` (plural)
* The "single **Composite Item**" key is `composite_item` (singular)
* The key for the unique ID of each **Composite Item** is `composite_item_id`

Further inspection of the API docs indicate that, in addition the usual
_Create_, _Retrieve_, _Update_, _Delete_ and _List All_ operations, we can also
perform _Mark as Active_ and _Mark as Inactive_ operations.

### Add the class
ZohoObject classes are created by the `ZohoObjectFactory()` function
in `pyzohoapi/objecttypes/__init__.py`. In this case, we use:
```{code-block} python
CompositeItem = ZohoObjectFactory("CompositeItem", nameform="composite_item", idform="composite_item", mixins=[WithActivate])
```

* _CompositeItem = ..._ is the Python class name exposed by `pyzohoapi.objecttypes`.
* _"CompositeItem"..._ will be pluralized and lowercased to create the URL fragment.
* _nameform="composite_item"..._ defines the keys (singular and plural) of the objects in the JSON response data. This is only needed if `nameform` is different from the lowercased first parameter.
* _idform="composite_item"..._ defines the root of the key used to determine the ID and Number (when available) of the object. So the ID and Number keys are `{idform}_id` and `{idform}_number`. This is only needed if `idform` is different from the lowercased first parameter.
* _mixins=[WithActivate]..._ adds the `Activate()` and `Deactivate()` operations by way of a mixin in `pyzohoapi.objecttypes.mixins`; keep reading for how that works.

## Extending ZohoObject Classes
The `pyzohoapi.objecttypes.mixins` module contains classes which expose one
or more additional methods to add to particular object types. In the example
above, we've mixed in `WithActivate` class, which adds the `Activate()` and
`Deactive()` methods to the `CompositeItem` class. See [Type-Specific
Methods](/objrefs/methods.md) for the breakdown of the existing methods.

### Examine the API Docs
We'll look at the existing mixin `WithActivate` as an example.

Looking at the API Docs, we see that there are several different Zoho objects
which support the "Mark as Active" and "Mark as Inactive" operations. Every
object either supports both or neither of these operations.

We also see that the method for performing these operations is of the form:

`post /{object-url-fragment}/{object-id}/{active|inactive}`

These factors suggest we create a mixin class which implements a method handling
the `post` to Zoho, and methods to expose both operations. This class, then, can
be applied to the appropriate object types.

### Create a Mixin Class
```{code-block} python
class WithActivate:
    ...
```
The pattern for the class name is `With{Feature}`.

### Create Internal Method(s)
```{code-block} python
:emphasize-lines: 2
class WithActivate:
    def _do_operation(self, status, funcname):
        ...
```
This is optional, but since in this case there are two, basically identical,
operations we want to expose, we'll build an internal method to actually perform
the operation.

Internal method names should begin with `_`, both to indicate they are "private"
and to avoid collision with Zoho object field names.

In this case, we need the new status ('active' or 'inactive', per the API docs),
and the name of the function being called (for exceptions).

### Ensure the Operation is Valid
```{code-block} python
:emphasize-lines: 3, 5
class WithActivate:
    def _do_operation(self, status, funcname):
        if self._id and self._data:
            ...
        raise ZohoInvalidOpError(funcname, self)
```
This operation is only valid on single objects (they have an `_id`) and which
already exist (they have `_data`). If those conditions aren't met, we'll raise a
`ZohoInvalidOpError`.

### Perform the API Call
```{code-block} python
:emphasize-lines: 4-9
class WithActivate:
    def _do_operation(self, status, funcname):
      if self._id and self._data:
          try:
              self._api.post(self._url_fragment(extraPath=[status]))
              self.status = status
              return True
          except ZohoException as e:
              return False
      raise ZohoInvalidOpError(funcname, self)
```
In order to `post` to the API, we use the API object's `post()` method. We have
to tell `post()` where to post to, which is what our `_url_fragment()` functions
does. It constructs the object-specific portion of the eventual URL with our
object type (i.e. `/compositeitems`), our ID (if appropriate), and adds anything
in the `extraPath` parameter. The API object takes care of the
`https://{whatever}.zoho.{whatever}`.

In this case, if `post()` raises an exception, we suppress it and return `False`.

### Create Public Method(s)
```{code-block} python
:emphasize-lines: 3-7
class WithActivate:
    ...
    def Activate(self):
        return self._do_operation('active', "Activate")

    def Deactivate(self):
        return self._do_operation('inactive', "Deactivate")
```
Public Method names should be CamelCase, for reasons noted elsewhere. Parameters
are operation-specific.

## Adding a New API Object
### Create a Module for the API
See `pyzohoapi/inventory.py` as an example.

### Define the Class
Inherit from `ZohoAPIBase`.
```{code-block} python
from .core import ZohoAPIBase
...
class ZohoInventory(ZohoAPIBase):
```

### Set the OAuth Scope
```{code-block} python
:emphasize-lines: 4
from .core import ZohoAPIBase
...
class ZohoInventory(ZohoAPIBase):
    _scope = "ZohoInventory.FullAccess.all"
```

### (Optional) Determine Available Regions
Override the `_regionmap` member if the API isn't available in every Zoho data
center. See the code for `ZohoAPIBase` for a guidance.

### Write `get_endpoint()`
The `get_endpoint()` method returns the endpoint of the api.
```{code-block} python
:emphasize-lines: 6-7
from .core import ZohoAPIBase
...
class ZohoInventory(ZohoAPIBase):
    _scope = "ZohoInventory.FullAccess.all"

    def get_endpoint(self, region):
        return f"https://inventory.zoho.{self._regionmap[region]}/api/v1"
```

### Expose Available ZohoObjects
```{code-block} python
:emphasize-lines: 2, 10-12
from .core import ZohoAPIBase
from . import objecttypes
...
class ZohoInventory(ZohoAPIBase):
    _scope = "ZohoInventory.FullAccess.all"

    def get_endpoint(self, region):
        return f"https://inventory.zoho.{self._regionmap[region]}/api/v1"
    ...
    def Account(self, *args, **kwargs): return objecttypes.Account(self, *args, **kwargs)
    def Bundle(self, *args, **kwargs): return objecttypes.Bundle(self, *args, **kwargs)
    ...
```
### Expose the module
In `pyzohoapi.__init__.py`, import the module and add it to the `__all__` list.
```{code-block} python
from .inventory import ZohoInventory
__all__ = ["ZohoInventory", ...]
```
