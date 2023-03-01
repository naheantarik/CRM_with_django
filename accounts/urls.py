from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('product/', views.product, name='product'),
    path('customer/<str:cng>/', views.customer, name='customer'),

    path('order/', views.createOrder, name='create_order'),
    path('update_order/<str:pk>/', views.update_order, name='update_order'),
    path('delete_order/<str:pk>/', views.deleteOrder, name='delete_order'),

    path('CreateProduct/', views.createProduct, name='CreateProduct'),
    path('delete_product/<str:pd>/', views.deleteProduct, name='delete_product'),
]
