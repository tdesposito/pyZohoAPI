# Exceptions
All exceptions we raise (other than basic Python exceptions like KeyError) are
subclasses of **ZohoException**.

## ZohoAPICallsExceeded
Raised if the operation on the object exceeded our allotment of API calls.

## ZohoAPIThrottled
Raised if we are throttled for too many concurrent requests or calling the API
too rapidly, and our back-off limits were exceeded.

## ZohoAuthRefreshFailure
Raised if an attempt to refresh our Access Token fails.

## ZohoInsufficentAuthKeys
Raised if we don't have all the OAuth parameters we need to authenticate.

## ZohoInvalidOpError
Raised if an operation on an object is invalid, for example calling **Create()**
on an existing object.

## ZohoUnknownRegionException
Raised if you try to create an API object with either an invalid region, or a
region not supported by the API.
