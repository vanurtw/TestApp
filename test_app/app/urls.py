from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import CustomerAPIViewSet, LotAPIViewSet

router = SimpleRouter()
router.register('customers', CustomerAPIViewSet, basename='customer')
router.register('lots', LotAPIViewSet, basename='lot')

urlpatterns = [
    path('', include(router.urls)),

]
