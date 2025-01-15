from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from .serializers import CustomerSerializer, LotSerializer
from .models import Customer, Lot
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

ValidateSchema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={'error': openapi.Schema(description='detail', type=openapi.TYPE_STRING)}
)

ErrorObject = openapi.Schema(
    type=openapi.TYPE_STRING,
)


class CustomerAPIViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['customer_inn', 'is_organization', 'is_person']
    search_fields = ['$customer_code', '$customer_name']
    ordering_fields = ['customer_name', 'customer_legal_address']

    def get_serializer_class(self):
        return CustomerSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['action'] = self.action
        return context

    def get_queryset(self):
        return Customer.objects.all()

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('customer_inn', openapi.IN_QUERY, type=openapi.TYPE_STRING, description='ИНН'),
            openapi.Parameter('is_organization', openapi.IN_QUERY, type=openapi.TYPE_BOOLEAN, description='Юр. лицо'),
            openapi.Parameter('is_person', openapi.IN_QUERY, type=openapi.TYPE_BOOLEAN, description='Физ. лицо'),
            openapi.Parameter('search', openapi.IN_QUERY, type=openapi.TYPE_STRING,
                              description='Поиск по наименованию и коду контрагента'),
            openapi.Parameter('ordering', openapi.IN_QUERY, type=openapi.TYPE_STRING,
                              description='Сортировка по наименованию и Юр. адрес: customer_name/customer_legal_address'),
        ]
    )
    def list(self, request, *args, **kwargs):
        '''Чтение всех записей контрагентов'''
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        responses={
            404: openapi.Response(description='Объект не найден', schema=ErrorObject)
        }
    )
    def retrieve(self, request, *args, **kwargs):
        '''Чтение конкретной записи контрагентов по id'''
        return super().retrieve(request, *args, **kwargs)

    def perform_update(self, serializer):
        serializer.save()

    @swagger_auto_schema(
        responses={
            404: openapi.Response(description='Объект не найден'),
            400: openapi.Response(description='Ошибка валидации', schema=ValidateSchema)
        }
    )
    def partial_update(self, request, *args, **kwargs):
        '''Частичное обновление записи контрагентов'''
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)


class LotAPIViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['nbs_rate', 'currency_code']
    search_fields = ['$customer_code__customer_name', 'date_delivery']
    ordering_fields = ['price', 'date_delivery']

    def get_serializer_class(self):
        return LotSerializer

    def get_queryset(self):
        return Lot.objects.all()

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['action'] = self.action
        return context

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('search', openapi.IN_QUERY, type=openapi.TYPE_STRING,
                              description='Поиск по наименованию контрагента и дате доставки'),
            openapi.Parameter('ordering', openapi.IN_QUERY, type=openapi.TYPE_STRING,
                              description='Сортировка по цене и дате доставки: price/date_delivery'),
        ]
    )
    def list(self, request, *args, **kwargs):
        '''Чтение всех записей лотов'''
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        responses={
            404: openapi.Response(description='Объект не найден', schema=ErrorObject)
        }
    )
    def retrieve(self, request, *args, **kwargs):
        '''Чтение конкретной записи лотов по id'''
        return super().retrieve(request, *args, **kwargs)

    def perform_update(self, serializer):
        serializer.save()

    @swagger_auto_schema(
        responses={
            404: openapi.Response(description='Объект не найден'),
            400: openapi.Response(description='Ошибка валидации', schema=ValidateSchema)
        }
    )
    def partial_update(self, request, *args, **kwargs):
        '''Частичное обновление записи лота'''
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
