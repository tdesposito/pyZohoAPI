# This file is part of pyZohoAPI, Copyright (C) Todd D. Esposito 2021.
# Distributed under the MIT License (see https://opensource.org/licenses/MIT).

from ...exceptions import *

from .CompositeItemOps import WithBundle

class WithActivate:
    """Adds `Activate()` and `Deactivate()`"""
    def _do_operation(self, status, funcname):
        if self._id and self._data:
            try:
                self._api.post(self._url_fragment(extraPath=[status]))
                self.status = status
                return True
            except ZohoException as e:
                return False
        raise ZohoInvalidOpError(funcname, self)

    def Activate(self):
        return self._do_operation('active', "Activate")

    def Deactivate(self):
        return self._do_operation('inactive', "Deactivate")


class WithImage:
    """Adds `AddImage()`, `DeleteImage()` and `GetImage()`"""
    def AddImage(self, name, image, type="image/jpeg"):
        if self._id:
            file = {'image': (name, image, type)}
            return self._api.post(self._url_fragment(extraPath=['image']), files=file)
        raise ZohoInvalidOpError("AddImage", self)

    def DeleteImage(self):
        if self._id:
            return self._api.delete(self._url_fragment(extraPath=['image']))
        raise ZohoInvalidOpError("AddImage", self)

    def GetImage(self):
        if self._id and self._data:
            return self._api.get(self._url_fragment(extraPath=['image']), "")
        raise ZohoInvalidOpError("GetImage", self)


class _WithStatus:
    def _mark(self, status):
        if self._id:
            try:
                self._api.post(self._url_fragment(extraPath=['status', status]))
                return True
            except ZohoException as e:
                return False
        return None


class WithConfirm(_WithStatus):
    """Adds `Confirm()`"""
    def Confirm(self):
        if not self._id:
            raise ZohoInvalidOpError("Confirm", self)
        return self._mark('confirmed')


class WithDraft(_WithStatus):
    """Adds `Draft()`"""
    def Draft(self):
        if not self._id:
            raise ZohoInvalidOpError("Draft", self)
        return self._mark('draft')


class WithVoid(_WithStatus):
    """Adds `Void()`"""
    def Void(self):
        if not self._id:
            raise ZohoInvalidOpError("Void", self)
        return self._mark('void')


class _WithAspect:
    def _updateAspect(self, aspect, aspect_id, data):
        data = self._api.put(self._url_fragment(extraPath=[aspect, aspect_id]), data, "")
        if data['code'] == 0:
            return True
        return False


class WithAddresses(_WithAspect):
    """Adds `UpdateBilling()` and `UpdateShipping()`"""
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
