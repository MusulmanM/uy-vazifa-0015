from django.urls import path
from .models import Category, Product
from .views import CategoryApiView, ProductApiView

urlpatterns = [
    path("category/", CategoryApiView.as_view()),
    path("product/", ProductApiView.as_view()),
]
