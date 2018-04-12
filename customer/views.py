from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import Address, Department, Customer
from .forms import AddressForm, DepartmentForm, CustomerForm


class AddressListView(ListView):
    model = Address


class AddressCreateView(CreateView):
    model = Address
    form_class = AddressForm


class AddressDetailView(DetailView):
    model = Address


class AddressUpdateView(UpdateView):
    model = Address
    form_class = AddressForm


class DepartmentListView(ListView):
    model = Department


class DepartmentCreateView(CreateView):
    model = Department
    form_class = DepartmentForm


class DepartmentDetailView(DetailView):
    model = Department


class DepartmentUpdateView(UpdateView):
    model = Department
    form_class = DepartmentForm


class CustomerListView(ListView):
    model = Customer


class CustomerCreateView(CreateView):
    model = Customer
    form_class = CustomerForm


class CustomerDetailView(DetailView):
    model = Customer


class CustomerUpdateView(UpdateView):
    model = Customer
    form_class = CustomerForm

