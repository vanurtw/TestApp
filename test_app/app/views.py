from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin
from .serializers import CustomerSerializer
from .models import Customer


class CustomerAPIViewSet(GenericViewSet, ListModelMixin):
    def get_serializer_class(self):
        return CustomerSerializer

    def get_queryset(self):
        return Customer.objects.all()

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
