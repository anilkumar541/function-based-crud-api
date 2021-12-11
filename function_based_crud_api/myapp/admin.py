from django.contrib import admin

# Register your models here.

from myapp.models import Products

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display=["id", "product_name", "created_at", "updated_at"]
    