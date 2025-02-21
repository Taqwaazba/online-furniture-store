from django.contrib import admin
from .models import Furniture

# Register your models here.

@admin.register(Furniture)
class FurnitureAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'created_at')
    search_fields = ('name', 'category')
