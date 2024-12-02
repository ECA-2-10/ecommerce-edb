from django.urls import path
from . import views

urlpatterns = [
    path('', views.order_search, name='order_search'),
    path('order-from-email', views.order_from_email, name='order_from_email'),
]