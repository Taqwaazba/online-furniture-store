from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FurnitureViewSet
from .views.inventory import InventoryViewSet

router = DefaultRouter()
router.register(r'furniture', FurnitureViewSet, basename='furniture')
router.register(r'inventory', InventoryViewSet, basename='inventory')

urlpatterns = [
    path('', include(router.urls)),
    path('inventory/search/', InventoryViewSet.as_view({'get': 'search'}), name='inventory-search'),
]