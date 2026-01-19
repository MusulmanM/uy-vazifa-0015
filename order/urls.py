from django.urls import path

from .views import OrderItemApiView, OrderApiView

urlpatterns = [
    path("order/", OrderApiView.as_view()),
    path("orderitem/", OrderItemApiView.as_view()),
]
