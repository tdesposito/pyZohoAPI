---
hide-toc: true
---
You are reading pyZohoAPI's documentation
=========================================

```{caution}
This is **BETA** software, and will be subject to changes in both
interface and behavior. Use at your own risk.
```

## About pyZohoAPI
 **pyZohoAPI** provides Pythonic access to Zoho APIs in the Finance Plus suite:
_Books, Checkout, Expense, Inventory, Invoice, and Subscriptions_.

```{note}
As of this release, we only have support for _Inventory_, and not every
object therein. Full support will be built out incrementally over future releases.

_Books_ support is in the code, but nascent and untested.
```

This package provides Python objects which correlate to the objects exposed by
the Zoho API. The Python objects provide a simple way to access, update, create,
delete and modify Zoho objects. We don't strive to encapsulate operations Zoho
performs in its clients; that's up to your code.

```{toctree}
:caption: Documentation
:hidden:
quickstart
userguide/index
objrefs/index
```

```{toctree}
:caption: Contributing
:hidden:
contrib/index
license
GitHub Repository <https://github.com/tdesposito/pyZohoAPI>
```
