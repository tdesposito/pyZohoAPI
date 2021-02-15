# This file is part of pyZohoAPI, Copyright (C) Todd D. Esposito 2021.
# Distributed under the MIT License (see https://opensource.org/licenses/MIT).

class ZohoException(Exception):
    def __init__(self, msg="Unspecified Error"):
        super().__init__(msg)

#---------------------------------------------------------------------------
# Exceptions raised by API objects

class ZohoAuthRefreshFailure(ZohoException):
    def __init__(self):
        super().__init__("Unable to refresh access token")


class ZohoInsufficentAuthKeys(ZohoException):
    def __init__(self):
        super().__init__("Unable to generate Authorization header")


class ZohoUnknownRegionException(ZohoException):
    def __init__(self, region):
        super().__init__(f'Unknown Region "{region}"')


#---------------------------------------------------------------------------
# Exceptions raised by Zoho objects

class ZohoAPICallsExceeded(ZohoException):
    def __init__(self):
        super().__init__("No API Calls remaining")


class ZohoAPIThrottled(ZohoException):
    def __init__(self):
        super().__init__("API Throttled")


class ZohoInvalidOpError(ZohoException):
    def __init__(self, op, target):
        if target.ID is false:
            super().__init__(f"Can't call {op} on a deleted {target.__class__.__name__}")
        elif target.IsList:
            super().__init__(f"Can't call {op} on a list-of {target.__class__.__name__}")
        else:
            # TODO: revise this message, provided we find a use for it
            super().__init__(f"Can't call {op} on an object of type {target.__class__.__name__}")
