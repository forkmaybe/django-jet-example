from django.contrib import admin
from django import forms
from .models import Address, Department, Customer


class AddressInline(admin.TabularInline):
    model = Address


class AddressAdminForm(forms.ModelForm):

    class Meta:
        model = Address
        fields = '__all__'


class AddressAdmin(admin.ModelAdmin):
    form = AddressAdminForm
    list_display = ['full_address', 'postcode']

admin.site.register(Address, AddressAdmin)


class DepartmentAdminForm(forms.ModelForm):

    class Meta:
        model = Department
        fields = '__all__'


class DepartmentAdmin(admin.ModelAdmin):
    form = DepartmentAdminForm
    list_display = ['name']

admin.site.register(Department, DepartmentAdmin)


class CustomerAdminForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = '__all__'


class CustomerAdmin(admin.ModelAdmin):
    form = CustomerAdminForm
    list_display = ['dob', 'position']
    inlines = [
        AddressInline,
    ]

admin.site.register(Customer, CustomerAdmin)
