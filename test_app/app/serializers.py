from rest_framework import serializers
from .models import Customer, Lot
from rest_framework.exceptions import ValidationError


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
        customer_code_main = self.initial_data.get('customer_code_main', None)
        if customer_code_main:
            try:
                obj.customer_code_main_id = customer_code_main
                obj.save()
            except Exception as ex:
                raise ValidationError(str(ex))
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


class LotSerializer(serializers.ModelSerializer):
    customer_code = serializers.SerializerMethodField()

    def get_customer_code(self, obj, *args, **kwargs):
        customer_code = self.initial_data.get('customer_code', None)
        if customer_code:
            try:
                obj.customer_code_id = customer_code
                obj.save()
            except Exception as ex:
                raise ValidationError(str(ex))

        if obj.customer_code:
            serializer = CustomerReviewSerializer(obj.customer_code)
            return serializer.data

    class Meta:
        model = Lot
        fields = [
            'id',
            'lot_name',
            'customer_code',
            'price',
            'currency_code',
            'nbs_rate',
            'place_delivery',
            'date_delivery'
        ]
