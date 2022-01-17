# pyZohoAPI (v0.10.0)

**pyZohoAPI** provides Pythonic access to Zoho APIs in the Finance Plus suite:

* **Books**
* *Checkout*<sup>*</sup>
* *Expense*<sup>*</sup>
* **Inventory**
* *Invoice*<sup>*</sup>
* *Subscriptions*<sup>*</sup>

<sup>*</sup> Support is planned, but not yet available.

[![PyPI](https://img.shields.io/pypi/v/pyzohoapi)](https://pypi.org/project/pyzohoapi/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pyzohoapi)](https://pypi.org/project/pyzohoapi/)
![License](https://img.shields.io/github/license/tdesposito/pyZohoAPI)
[![Documentation Status](https://readthedocs.org/projects/pyzohoapi/badge/?version=latest)](https://pyzohoapi.readthedocs.io/en/latest/?badge=latest)

## Installing pyZohoAPI

<!-- start installation -->

You'll need at least **Python 3.6** to install pyZohoAPI.

### Via PyPI

```console
$ python -m pip install pyzohoapi
```

### From Source

We use [Poetry](https://python-poetry.org/) for virtual environment and
dependency management.

```console
$ git clone https://github.com/tdesposito/pyZohoAPI.git
$ cd pyZohoAPI
$ poetry install
$ poetry build
$ pip install dist/*.whl
```
<!-- end installation -->

## Basic Usage

<!-- start basic-usage -->

```python
>>> from pyzohoapi import ZohoInventory
>>> api = ZohoInventory("{your-orginization-id}", "{your-region}",
...   client_id="{your-client-id}",
...   client_secret="{your-client-secret}",
...   refresh_token="{your-refresh-token}"
... )
>>> contact = api.Contact(email="test@example.com").First()
>>> contact.IsLoaded
True
>>> contact.first_name
'test'
>>> contact.first_name = "Changed"
>>> contact.Update()
```
<!-- end basic-usage -->

See the [full documentation on ReadTheDocs](https://pyzohoapi.readthedocs.io/en/latest/).

## Contributing

[Pull Requests](https://github.com/tdesposito/pyZohoAPI/pulls) gladly
considered! Please use our pull request template when submitting your pull
request.

| Thanks Contributors! |
| :------------------: |
| ![Shubham Agawane](https://avatars.githubusercontent.com/s-agawane?size=80) 
[Shubham Agawane](https://github.com/s-agawane) |
