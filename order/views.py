from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import OrderItem, Orders
from .serializer import OrderItemSerializer, OrdersSerializer


class OrderItemApiView(APIView):
    def get(self, request):
        orderitems = OrderItem.objects.all()
        data = OrderItemSerializer(orderitems, many=True)
        return Response(data.data)

    def post(self, request):
        new_orderitem = OrderItemSerializer(data=request.data)
        if new_orderitem.is_valid():
            new_orderitem.save()

            return Response({"message": "orderitem"})
        return Response({"message": "jefe qwfeqioewjir"})


class OrderApiView(APIView):
    def get(self, request):
        order = Orders.objects.all()
        data = OrdersSerializer(order, many=True)
        return Response(data.data)

    def post(self, request):
        new_order = OrdersSerializer(data=request.data)
        if new_order.is_valid():
            new_order.save()

            return Response({"message": "orderr"})
        return Response({"message": "enjfle"})
