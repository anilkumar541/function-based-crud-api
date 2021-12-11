from django.db import models

# Create your models here.

class Products(models.Model):
    product_name = models.CharField(max_length=44)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
