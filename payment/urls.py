from django.urls import path

from . import views

app_name = 'payment'

urlpatterns = [
    path('', views.payment_process, name='process'),
    path('create-checkout/', views.create_checkout_session, name='create-checkout'),
    path('success/', views.payment_success, name='success'),
    path('cancel/', views.payment_cancel, name='cancel'),
]