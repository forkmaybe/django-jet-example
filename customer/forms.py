from django import forms
from .models import Address, Department, Customer


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['full_address', 'postcode', 'customer']


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name']


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['dob', 'position', 'user', 'department']


