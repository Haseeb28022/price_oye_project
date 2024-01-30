from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrderViewSet
from .views import OrderDetailViewSet
from .views import CategoryViewSet

router = DefaultRouter()
router.register(r'orders', OrderViewSet, basename='orders')
router.register(r'order_details', OrderDetailViewSet, basename='orderDetails')
router.register(r'cart', CategoryViewSet, basename='cart')

urlpatterns = [
    path('', include(router.urls)),
    # Add other app URLs here
]
