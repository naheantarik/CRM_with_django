from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('product/', views.product, name='product'),
    path('customer/<str:cng>/', views.customer, name='customer'),

    path('order/', views.createOrder, name='create_order'),
    path('update_order/<str:pk>/', views.update_order, name='update_order'),
    path('delete_order/<str:pk>/', views.deleteOrder, name='delete_order'),

    path('create_product/', views.createProduct, name='create_product'),
]
