from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Category, Product
from .serializer import CatigorySerializer, ProductSerializer


class CategoryApiView(APIView):
    def get(self, request):
        categores = Category.objects.all()
        data = CatigorySerializer(categores, many=True)
        return Response(data.data)

    def post(self, request):
        new_category = CatigorySerializer(data=request.data)
        if new_category.is_valid():
            new_category.save()

            return Response({"message": "category"})
        return Response({"message": "jefioewjir"})


class ProductApiView(APIView):
    def get(self, request):
        products = Product.objects.all()
        data = ProductSerializer(products, many=True)
        return Response(data.data)

    def post(self, request):

        return Response({"message": "okkkkkkkkkkkk"})
