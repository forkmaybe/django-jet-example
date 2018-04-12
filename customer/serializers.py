from . import models

from rest_framework import serializers


class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Address
        fields = (
            'pk', 
            'full_address', 
            'postcode', 
        )


class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Department
        fields = (
            'pk', 
            'name', 
        )


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Customer
        fields = (
            'pk', 
            'dob', 
            'position', 
        )


