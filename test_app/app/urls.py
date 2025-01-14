from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import CustomerAPIViewSet

router = SimpleRouter()
router.register('customer', CustomerAPIViewSet, basename='customer')

urlpatterns = [
    path('', include(router.urls)),

]
