from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FurnitureViewSet
from .views import InventoryViewSet
from .views import RegisterUserView, LoginUserView, UserProfileView
from .views import ShoppingCartViewSet
from .views import OrderViewSet
from .views import CheckoutViewSet

router = DefaultRouter()
router.register(r'furniture', FurnitureViewSet, basename='furniture')
router.register(r'inventory', InventoryViewSet, basename='inventory')
router.register(r'shopping-cart', ShoppingCartViewSet, basename='shopping-cart')
router.register(r'order', OrderViewSet, basename='order')
router.register(r'checkout', CheckoutViewSet, basename='checkout')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/register/', RegisterUserView.as_view(), name='register'),
    path('auth/login/', LoginUserView.as_view(), name='login'),
    path('auth/profile/', UserProfileView.as_view(), name='profile'),
    path('inventory/search/', InventoryViewSet.as_view({'get': 'search'}), name='inventory-search'),
]