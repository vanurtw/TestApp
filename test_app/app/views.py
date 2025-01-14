from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from .serializers import CustomerSerializer, LotSerializer
from .models import Customer, Lot
from rest_framework.response import Response


class CustomerAPIViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    def get_serializer_class(self):
        return CustomerSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['action'] = self.action
        return context

    def get_queryset(self):
        return Customer.objects.all()

    def list(self, request, *args, **kwargs):
        '''Чтение всех записей контрагентов'''
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        '''Чтение конкретной записи контрагентов по id'''
        return super().retrieve(request, *args, **kwargs)

    def perform_update(self, serializer):
        serializer.save()

    def partial_update(self, request, *args, **kwargs):
        '''Частичное обновление записи контрагентов'''
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)


class LotAPIViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    def get_serializer_class(self):
        return LotSerializer

    def get_queryset(self):
        return Lot.objects.all()

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['action'] = self.action
        return context

    def list(self, request, *args, **kwargs):
        '''Чтение всех записей лотов'''
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        '''Чтение конкретной записи лотов по id'''
        return super().retrieve(request, *args, **kwargs)

    def perform_update(self, serializer):
        serializer.save()

    def partial_update(self, request, *args, **kwargs):
        '''Частичное обновление записи лота'''
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
