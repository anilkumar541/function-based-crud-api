from myapp.models import Products
from rest_framework import serializers

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Products
        fields=["id", "product_name", "created_at", "updated_at"]
        
