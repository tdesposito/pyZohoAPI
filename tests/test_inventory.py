# This file is part of pyZohoAPI, Copyright (C) Todd D. Esposito 2021.
# Distributed under the MIT License (see http://opensource.org/licenses/MIT).

from pprint import pprint

import pytest

from pyzohoapi.inventory import ZohoInventory
from pyzohoapi.exceptions import ZohoException

from private import testdata

z = ZohoInventory(testdata['orgid'], testdata['region'], **testdata['api'])

def test_empty_user():
    c = z.User()
    assert not c.IsLoaded


def test_get_user():
    c = z.User(testdata['inventory']['user']['id'])
    assert c.IsLoaded
    assert not c.IsList
    assert c.email == testdata['inventory']['user']['email']


def test_search_user():
    c = z.User(email=testdata['inventory']['user']['email'])
    assert c.IsLoaded
    assert c.IsList
    assert repr(c) == "List of User objects"
    one = c.First()
    assert one.IsLoaded
    assert one.ID == testdata['inventory']['user']['id']


def test_search_notfound():
    c = z.User(email=testdata['inventory']['user']['invalid-email'])
    assert c.IsLoaded
    assert c.IsList
    assert repr(c) == "List of User objects"
    assert len(c._data.to_python()) == 0
    one = c.First()
    assert repr(one) == "New User"


def test_list_raw_user():
    c = z.User()
    assert not c.IsLoaded
    for i in c.Iter(raw=True):
        assert hasattr(i, 'user_id')


def test_filter_list_raw_user():
    c = z.User()
    assert not c.IsLoaded
    count = 0
    for i in c.Iter(raw=True, email=testdata['inventory']['user']['email']):
        count += 1
        assert i.get('email') == testdata['inventory']['user']['email']
    assert count == 1


def test_list_user():
    c = z.User()
    assert not c.IsLoaded
    for i in c.Iter():
        assert i.__class__.__name__ == "User"


def test_filter_list_user():
    c = z.User()
    assert not c.IsLoaded
    count = 0
    for i in c.Iter(email=testdata['inventory']['user']['email']):
        count += 1
        assert i.__class__.__name__ == "User"
        assert i.IsLoaded
        assert i.email == testdata['inventory']['user']['email']
    assert count == 1


def test_so_get_related():
    so = z.SalesOrder(testdata['inventory']['salesorder']['id'])
    assert so.IsLoaded
    assert so.Number == testdata['inventory']['salesorder']['number']
    cust = so.GetRelated(z.Contact, "customer_id")
    assert cust.IsLoaded
    assert cust.contact_name == testdata['inventory']['salesorder']['contact_name']


def test_so_iter_related():
    so = z.SalesOrder(testdata['inventory']['salesorder']['id'])
    assert so.IsLoaded
    for item in so.IterRelatedList(z.Item, "line_items", "item_id"):
        assert item.IsLoaded
        assert item.sku == testdata['inventory']['salesorder']['line_item_sku']
        break


def test_so_map_related():
    so = z.SalesOrder(testdata['inventory']['salesorder']['id'])
    assert so.IsLoaded
    for item in so.MapRelatedList(z.Item, "line_items", "item_id"):
        assert item.object.IsLoaded
        assert item.meta.sku == testdata['inventory']['salesorder']['line_item_sku']
        assert item.meta.sku == item.object.sku
        break

def test_create_customer():
    c = z.Contact()
    c.contact_name = "00 TEST CONTACT - DO NOT USE"
    c.contact_type = "customer"
    c.customer_sub_type = "individual"
    c.contact_persons= [{
                        'first_name': "00 Test",
                        'last_name': " Contact",
                        'email': "test@example.com",
                        'phone': "123-456-7890",
                        'is_primary_contact': True,
                    }]
    c.is_taxable = True
    c.tax_id = testdata['inventory']['newuser']['tax_id']
    c.tax_name = testdata['inventory']['newuser']['tax_name']
    c.payment_terms = testdata['inventory']['newuser']['payment_terms']
    c.payment_terms_label = testdata['inventory']['newuser']['payment_terms_label']

    c.Create()
    assert c.ID is not None
    testdata['inventory']['newuser'] = {'id': c.ID}


def test_update_customer():
    assert testdata['inventory'].get('newuser',{}).get('id', False)
    c = z.Contact(testdata['inventory']['newuser']['id'])
    assert c.IsLoaded
    assert c.shipping_address.city == ""
    c.shipping_address = testdata['inventory']['newaddress']
    c.Update()
    del c
    c = z.Contact(testdata['inventory']['newuser']['id'])
    assert c.IsLoaded
    assert c.shipping_address.city == testdata['inventory']['newaddress']['city']


def test_delete_customer():
    assert testdata['inventory'].get('newuser',{}).get('id', False)
    c = z.Contact(testdata['inventory']['newuser']['id'])
    assert c.IsLoaded
    c.Delete()
    assert c.IsDeleted
