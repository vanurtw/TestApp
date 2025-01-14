from django.apps import AppConfig as AppConfigDjango


class AppConfig(AppConfigDjango):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'
