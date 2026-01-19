from rest_framework.serializers import ModelSerializer
from .models import OrderItem, Orders


class OrdersSerializer(ModelSerializer):
    class Meta:
        fields = ["user", "status", "total_price"]
        model = Orders


class OrderItemSerializer(ModelSerializer):
    class Meta:
        fields = ["order", "product", "quantity"]
        model = OrderItem
