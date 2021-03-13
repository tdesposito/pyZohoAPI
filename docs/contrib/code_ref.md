# Hacking the Internals

```{todo}
Lots to do here. Most of these docs are autodoc'ed from the code. More
docstrings there would be of great use.
```

This section documents the internals and public methods of pyZohoAPI.

## pyzohoapi.core
### ZohoAPIBase
```{eval-rst}
.. autoclass:: pyzohoapi.core.ZohoAPIBase
   :members:
```
### ZohoObjectBase
```{eval-rst}
.. autoclass:: pyzohoapi.core.ZohoObjectBase
  :members:
```

## pyzohoapi.core.collection
Internally, a ZohoObject's `_data` member is either a DottedList or a DottedDict.

This module is a modified version of
[DottedDict](https://github.com/carlosescri/DottedDict). I've stripped out all
the Python2 compatibility stuff, and added some fixes from the upstream open
pull requests.
```{eval-rst}
.. automodule:: pyzohoapi.core.collection
   :members:
```

## pyzohoapi.core.utils
```{eval-rst}
.. automodule:: pyzohoapi.core.utils
   :members:
```

## pyzohoapi.exceptions
```{eval-rst}
.. automodule:: pyzohoapi.exceptions
   :members:
```

## pyzohoapi.objecttypes
```{eval-rst}
.. automodule:: pyzohoapi.objecttypes
   :members:
```

## pyzohoapi.objecttypes.mixins
```{eval-rst}
.. automodule:: pyzohoapi.objecttypes.mixins
   :members:
```
