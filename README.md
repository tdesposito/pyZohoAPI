## pyZohoAPI (v0.1.1)
 **pyZohoAPI** provides Pythonic access to Zoho APIs in the Finance Plus suite:
 * Books
 * Checkout
 * Expense
 * Inventory
 * Invoice
 * Subscriptions

[![Documentation Status](https://readthedocs.org/projects/pyzohoapi/badge/?version=latest)](https://pyzohoapi.readthedocs.io/en/latest/?badge=latest)

### Installing pyZohoAPI
<!-- start installation -->

You'll need at least **Python 3.6** to install pyZohoAPI.

Via PyPI:
```console
$ python -m pip install pyzohoapi
```
<!-- end installation -->

### Basic Usage

<!-- start basic-usage -->
```python
>>> from pyzohoapi import ZohoInventory
>>> apiParams = {
... }
>>> inventory = ZohoInventory("{your-orginization-id}", "{your-region}",
...   client_id="{your-client-id}",
...   client_secret="{your-client-secret}",
...   refresh_token="{your-refresh-token}"
... )
>>> contact = inventory.Contact(email="test@example.com").First()
>>> contact.IsLoaded
True
>>> contact.first_name
'test'
>>> contact.first_name = "Changed"
>>> contact.Update()
```
<!-- end basic-usage -->

See the [full documetation on ReadTheDocs](https://pyzohoapi.readthedocs.io/en/latest/)

### Contributing
Pull Requests gladly considered!
