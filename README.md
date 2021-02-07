# pyZohoAPI - Pythonic access to the collection of Zoho REST APIs.

## Basic usage
```python
from pyzohoapi import ZohoInventory

inventory = ZohoInventory("123456", "us", client_id="987654", client_secret="xxxxyyyy", refresh_token="1000.4242424242")

customer = inventory.Contact(email="test@example.com").one()

```

**Current version:** 0.1.0
