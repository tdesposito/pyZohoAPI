# Logging

We register a standard Python `Logger` named `pyzohoapi`.

## Configuring Logging
Our logger only emits **DEBUG**-level LogRecords; in order to get these messages
into your application's logs, use, for example:

```{code-block} python
import logging
logging.basicConfig(level=logging.DEBUG)
```

However, since we use the `requests` package internally, the above will get you all the `urllib3` messages, which you may not want. This will filter those out handily:

```{code-block} python
logging.getLogger('urllib3.connectionpool').setLevel(logging.INFO)
```

## Activity we log
We emit `LogRecords` when we:

* request a new access token
* make an HTTP request (GET, DELETE, POST, PUT)
* pause to implement rate limiting
* exceed our API call limit
* pause before retrying an HTTP request
