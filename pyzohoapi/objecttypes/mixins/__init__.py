# This file is part of pyZohoAPI, Copyright (C) Todd D. Esposito 2021.
# Distributed under the MIT License (see https://opensource.org/licenses/MIT).

from ...exceptions import *

class WithActivate:
    def Activate(self):
        if self._id:
            data = self._api.post(self._url_fragment(extraPath=['active']))
            if data['code'] == 0:
                self.status = "active"
            return self
        raise ZohoInvalidOpError("Activate", self)

    def Deactivate(self):
        if self._id:
            data = self._api.post(self._url_fragment(extraPath=['inactive']))
            if data['code'] == 0:
                self.status = "inactive"
            return self
        raise ZohoInvalidOpError("Deactivate", self)


class WithImage:
    def AddImage(self, name, image, type="image/jpeg"):
        if self._id:
            file = {'image': (name, image, type)}
            return self._api.post(self._url_fragment(extraPath=['image']), files=file)
        raise ZohoInvalidOpError("AddImage", self)

    def DeleteImage(self):
        if self._id:
            return self


class _WithStatus:
    def _mark(self, status):
        if self._id:
            return self._api.post(self._url_fragment(extraPath=['status', status]))
        return None


class WithConfirm(_WithStatus):
    def Confirm(self):
        if not self._id:
            raise ZohoInvalidOpError("Confirm", self)
        self._mark('confirmed')
        return self


class WithDraft(_WithStatus):
    def Draft(self):
        if not self._id:
            raise ZohoInvalidOpError("Draft", self)
        self._mark('draft')
        return self


class WithVoid(_WithStatus):
    def Void(self):
        if not self._id:
            raise ZohoInvalidOpError("Void", self)
        self._mark('void')
        return self


class _WithAspect:
    def _updateAspect(self, aspect, aspect_id, data):
        data = self._api.put(self._url_fragment(extraPath=[aspect, aspect_id]), data, "")
        import pprint; pprint.pprint(data, indent=2)
        if data['code'] == 0:
            return True
        return False


class WithAddresses(_WithAspect):
    def UpdateBilling(self):
        if self._id and self._data:
            self._updateAspect('address', self.billing_address.address_id, self.billing_address.to_python())
            return self
        raise ZohoInvalidOpError("UpdateBilling", self)
    def UpdateShipping(self):
        if self._id and self._data:
            self._updateAspect('address', self.shipping_address.address_id, self.shipping_address.to_python())
            return self
        raise ZohoInvalidOpError("UpdateShipping", self)
