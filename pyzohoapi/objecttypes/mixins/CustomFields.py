# This file is part of pyZohoAPI, Copyright (C) Todd D. Esposito 2021.
# Distributed under the MIT License (see https://opensource.org/licenses/MIT).
import datetime

from ...core.collection import DottedList

from ...exceptions import *

class HasCustomFields:
    def GetCustomField(self, key, listKey="custom_fields", default=None):
        if self._id:
            if self._data:
                for cf in self._data.get(listKey, []):
                    if key in [cf['label'], cf['placeholder']]:
                        return cf['value']
            return default
        raise ZohoInvalidOpError("GetCustomField", self)

    def SetCustomField(self, key, value, listKey="custom_fields", altkey=None):
        """ Sets the value of an existing Custom Field

        :param key: Custom Field `placeholder` or `label` (string)
        :param value: new value for the Custom Field.
        :param listKey: key to the Custom Fields list. Defaults to "custom_fields".
        :param altkey: "alternate" key for adding a custom field.
        :return: `self`
        :raises ZohoInvalidOpError: If `self` isn't an existing object.
        """
        if self._id:
            if self._data:
                for cf in self._data.get(listKey, []):
                    if key in [cf['label'], cf['placeholder']]:
                        cf['value'] = value
                        return self
                # We didn't find the custom field, so we need to add it.
                self._data.setdefault(listKey, DottedList()).append({
                    'placeholder': key if key.startswith("cf_") else altkey,
                    'label': altkey if key.startswith("cf_") else key,
                    'value': value,
                })
            return self
        raise ZohoInvalidOpError("SetCustomField", self)
