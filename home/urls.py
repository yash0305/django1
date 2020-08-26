from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('products', views.products, name='products'),
    path('createOrder', views.createOrder, name='createOrder'),
    path('customer/<str:pk_test>/', views.customer, name='customer'),

]