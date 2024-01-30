from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PaymentViewSet
from .views import InvoiceViewSet

router = DefaultRouter()
router.register(r'payment', PaymentViewSet, basename='payments')
router.register(r'invoice', InvoiceViewSet, basename='invoices')

urlpatterns = [
    path('', include(router.urls)),
    # Add other app URLs here
]
