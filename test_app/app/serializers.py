from rest_framework import serializers
from .models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['customer_code', 'customer_name', 'customer_inn', 'customer_kpp', 'customer_legal_address',
                  'customer_postal_address', 'customer_email', 'customer_code_main', 'is_organization', 'is_person']
