from django.core.urlresolvers import reverse
from django_extensions.db.fields import AutoSlugField
from django.db.models import *
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.contrib.auth import models as auth_models
from django.db import models as models
from django_extensions.db import fields as extension_fields
from django.contrib.auth.models import User


class Department(models.Model):

    # Fields
    name = CharField(max_length=100)

    class Meta:
        ordering = ('-pk',)

    def __str__(self):
        return '{}'.format(self.name)

    def __unicode__(self):
        return u'%s' % self.name

    def get_absolute_url(self):
        return reverse('customer_department_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('customer_department_update', args=(self.pk,))


class Customer(models.Model):

    # Fields
    dob = DateField()
    position = CharField(max_length=50)

    # Relationship Fields
    user = OneToOneField(User, on_delete=models.CASCADE)
    department = ForeignKey(Department, on_delete=models.CASCADE)

    class Meta:
        ordering = ('-pk',)

    def __str__(self):
        return "{} {}".format(self.user.first_name, self.user.last_name)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_full_name(self):
        return self.__str__()

    def get_absolute_url(self):
        return reverse('customer_customer_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('customer_customer_update', args=(self.pk,))


class Address(models.Model):

    # Fields
    full_address = TextField()
    postcode = IntegerField()
    customer = ForeignKey(Customer, on_delete=models.CASCADE)

    class Meta:
        ordering = ('-pk',)

    def __str__(self):
        return "{}, postcode: {}".format(self.full_address, self.postcode)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('customer_address_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('customer_address_update', args=(self.pk,))
