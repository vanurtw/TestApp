from django.contrib import admin
from .models import Customer, Lot


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    '''Регистрация модели Customer в админ панели'''
    pass


@admin.register(Lot)
class LotAdmin(admin.ModelAdmin):
    '''Регистрация модели Lot в админ панели'''
    pass
