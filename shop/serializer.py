from rest_framework.serializers import ModelSerializer
from .models import Category, Product


class CatigorySerializer(ModelSerializer):
    class Meta:
        fields = ["name", "is_active"]
        model = Category


class ProductSerializer(ModelSerializer):
    class Meta:
        fields = ["name", "description", "created_at", "price"]
        model = Product
