import unittest
from django.core.urlresolvers import reverse
from django.test import Client
from .models import Address, Department, Customer
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType


def create_django_contrib_auth_models_user(**kwargs):
    defaults = {}
    defaults["username"] = "username"
    defaults["email"] = "username@tempurl.com"
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_django_contrib_auth_models_group(**kwargs):
    defaults = {}
    defaults["name"] = "group"
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_django_contrib_contenttypes_models_contenttype(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_address(**kwargs):
    defaults = {}
    defaults["full_address"] = "full_address"
    defaults["postcode"] = "postcode"
    defaults.update(**kwargs)
    if "customer" not in defaults:
        defaults["customer"] = create_customer()
    return Address.objects.create(**defaults)


def create_department(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults.update(**kwargs)
    return Department.objects.create(**defaults)


def create_customer(**kwargs):
    defaults = {}
    defaults["dob"] = "dob"
    defaults["position"] = "position"
    defaults.update(**kwargs)
    if "user" not in defaults:
        defaults["user"] = create_user()
    if "department" not in defaults:
        defaults["department"] = create_department()
    return Customer.objects.create(**defaults)


class AddressViewTest(unittest.TestCase):
    '''
    Tests for Address
    '''

    def setUp(self):
        self.client = Client()

    def test_list_address(self):
        url = reverse('customer_address_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_address(self):
        url = reverse('customer_address_create')
        data = {
            "full_address": "full_address",
            "postcode": "postcode",
            "customer": create_customer().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_address(self):
        address = create_address()
        url = reverse('customer_address_detail', args=[address.pk, ])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_address(self):
        address = create_address()
        data = {
            "full_address": "full_address",
            "postcode": "postcode",
            "customer": create_customer().pk,
        }
        url = reverse('customer_address_update', args=[address.pk, ])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class DepartmentViewTest(unittest.TestCase):
    '''
    Tests for Department
    '''

    def setUp(self):
        self.client = Client()

    def test_list_department(self):
        url = reverse('customer_department_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_department(self):
        url = reverse('customer_department_create')
        data = {
            "name": "name",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_department(self):
        department = create_department()
        url = reverse('customer_department_detail', args=[department.pk, ])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_department(self):
        department = create_department()
        data = {
            "name": "name",
        }
        url = reverse('customer_department_update', args=[department.pk, ])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class CustomerViewTest(unittest.TestCase):
    '''
    Tests for Customer
    '''

    def setUp(self):
        self.client = Client()

    def test_list_customer(self):
        url = reverse('customer_customer_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_customer(self):
        url = reverse('customer_customer_create')
        data = {
            "dob": "dob",
            "position": "position",
            "user": create_user().pk,
            "department": create_department().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_customer(self):
        customer = create_customer()
        url = reverse('customer_customer_detail', args=[customer.pk, ])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_customer(self):
        customer = create_customer()
        data = {
            "dob": "dob",
            "position": "position",
            "user": create_user().pk,
            "department": create_department().pk,
        }
        url = reverse('customer_customer_update', args=[customer.pk, ])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)
