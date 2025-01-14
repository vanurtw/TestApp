from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import CustomerAPIViewSet

router = SimpleRouter()
router.register('customers', CustomerAPIViewSet, basename='customer')

urlpatterns = [
    path('', include(router.urls)),

]
