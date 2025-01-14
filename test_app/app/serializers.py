from rest_framework import serializers
from .models import Customer


class CustomerReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = [
            'id',
            'customer_code',
            'customer_name'
        ]


class CustomerSerializer(serializers.ModelSerializer):
    customer_code_main = serializers.SerializerMethodField()

    def get_customer_code_main(self, obj, *args, **kwargs):
        if self.context.get('action') == 'partial_update':
            customer_code_main = self.initial_data.get('customer_code_main', obj.customer_code_main)
            obj.customer_code_main_id = customer_code_main
            obj.save()
        if obj.customer_code_main:
            serializer = CustomerReviewSerializer(obj.customer_code_main)
            return serializer.data

    class Meta:
        model = Customer
        fields = [
            'id',
            'customer_code',
            'customer_name',
            'customer_inn',
            'customer_kpp',
            'customer_legal_address',
            'customer_postal_address',
            'customer_email',
            'customer_code_main',
            'is_organization',
            'is_person'
        ]
