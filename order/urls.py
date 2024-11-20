from django.urls import path
from . import views

urlpatterns = [
    path('', views.order_search, name='order_search'),
]