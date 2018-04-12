from django.conf.urls import url, include
from rest_framework import routers

from . import api
from . import views

router = routers.DefaultRouter()
router.register(r'address', api.AddressViewSet)
router.register(r'department', api.DepartmentViewSet)
router.register(r'customer', api.CustomerViewSet)


urlpatterns = (
    # urls for Django Rest Framework API
    url(r'^api/v1/', include(router.urls)),
)

urlpatterns += (
    # urls for Address
    url(r'^address/$', views.AddressListView.as_view(), name='customer_address_list'),
    url(r'^address/create/$', views.AddressCreateView.as_view(), name='customer_address_create'),
    url(r'^address/detail/(?P<pk>\S+)/$', views.AddressDetailView.as_view(), name='customer_address_detail'),
    url(r'^address/update/(?P<pk>\S+)/$', views.AddressUpdateView.as_view(), name='customer_address_update'),
)

urlpatterns += (
    # urls for Department
    url(r'^department/$', views.DepartmentListView.as_view(), name='customer_department_list'),
    url(r'^department/create/$', views.DepartmentCreateView.as_view(), name='customer_department_create'),
    url(r'^department/detail/(?P<pk>\S+)/$', views.DepartmentDetailView.as_view(), name='customer_department_detail'),
    url(r'^department/update/(?P<pk>\S+)/$', views.DepartmentUpdateView.as_view(), name='customer_department_update'),
)

urlpatterns += (
    # urls for Customer
    url(r'^customer/$', views.CustomerListView.as_view(), name='customer_customer_list'),
    url(r'^customer/create/$', views.CustomerCreateView.as_view(), name='customer_customer_create'),
    url(r'^customer/detail/(?P<pk>\S+)/$', views.CustomerDetailView.as_view(), name='customer_customer_detail'),
    url(r'^customer/update/(?P<pk>\S+)/$', views.CustomerUpdateView.as_view(), name='customer_customer_update'),
)
