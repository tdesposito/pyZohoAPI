# API Objects
All operations start with one of the several product-specific API objects, each
named for the API they target.

Ideally, you create a single instance of any given API object, and use it for
the lifetime of your application.

## Creating an API Instance
Creating an API object follows this pattern:
```
api = ZohoProduct(organization_id, region="us", **apiArgs)
```
where _ZohoProduct_ is one of _ZohoBooks, ZohoCheckout, ZohoExpense,
ZohoInventory, ZohoInvoice, and ZohoSubscriptions_.

### Organization ID
You must pass your Organization ID as the first parameter to any API object's
constructor.

```{admonition} How to find your Organization ID
:class: seealso
From within the Zoho product WebUI, click on either the organization name or
your user avatar within the product header (far right). The Organization ID is
listed under each Organization you are a member of.
```
### API Region
Zoho operates in [several different data
centers](https://www.zoho.com/books/api/v3/#multidc), and which you use for your
API calls depends on where your product is running. You can pass in either the
Top-Level Domain name (ok, Australia's isn't _technically_ a TLD) or the
region's "friendly" name (case insensitive). These are:
  * Australia
  * Europe
  * India
  * US

## Other API Parameters
There are no mandatory parameters in this list, but the API won't function
without at least some of these.

The bare minimum are *access_token* and *expires_in*. But this only works if you
have a recent - less than an hour old - Access Token available to you from some
other channel.

In real usage, you're going to need client_id, client_secret, and refresh_token,
at a minimum.

In addition, there are several parameters which tune the package around Zoho's
API limits.

### client_id and client_secret
The Zoho OAuth client credentials.
```{admonition} How to find your Client ID and Secret
:class: seealso

From the [Zoho API Console](https://api-console.zoho.com), create or edit the
appropriate client type (depending on your application requirements). The Client
ID and Client Secret are available there.
```
```{warning}
Client ID and Secrets are just that: SECRET. Please don't include them directly
in any code you might share.
```

### intercall_delay
Determines the minimum amount of time, in seconds, between each API call.

**Default: 0**

### max_retries
Determines how many times, at most, we will retry a throttled call.

**Default: 10**

### max_retry_after
The longest time, in seconds, we are willing to wait to retry a throttled call.
If Zoho sends a **Retry-After** header of more than this amount, we'll abort the
call with an exception.

**Default: 180**

### min_calls_remaining
For Orgs/APIs with a per-day call limit, this is the minimum number of calls
that have to remain in our allotment for us to attempt a call. If there are
fewer than this, we raise an exception.

**Default: 1**
```{note}
Since we have to make at least one call to be informed how many calls remain, we
could, under certain circumstances, run you below this minimum, or even out of
calls.
```

### redirect_url
One of the Redirect URLs registered with the Zoho OAuth Client.

### refresh_token
One of your current, active Refresh Tokens, for use in creating Access Tokens.

```{admonition} How to get a Refresh Token.
:class: seealso

Zoho uses OAuth procedures to provide you Access and Refresh Tokens. Please see
[Zoho' API Documentation on OAuth](https://www.zoho.com/invtory/api/v1/#oauth) for
details.
```

### retry_backoff_seconds
The amount of time, in seconds, to wait between throttled calls, if Zoho doesn't
provide a **Retry-After** header.

**Default: 0.5**

```{todo}
Add Self-Client and Non-Browser Client instructions.
```
