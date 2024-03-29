from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginpage, name='login'),
    path('logout/', views.logoutPage, name='logout'),


    path('', views.home, name='home'),
    path('product/', views.product, name='product'),
    path('test/', views.api_response),
    path('customer/<str:cng>/', views.customer, name='customer'),
    path('customer_page/', views.customerPage, name='customer_page'),
    path('userPage/', views.user, name='userPage'),
    path('accountSet/', views.accountSet, name='accountSet'),

    # Order Update Delete Create

    path('create_order/<str:pk>/', views.createOrder, name='create_order'),
    path('update_order/<str:pk>/', views.update_order, name='update_order'),
    path('delete_order/<str:pk>/', views.deleteOrder, name='delete_order'),

    # Product Update Delete Create

    path('CreateProduct/', views.createProduct, name='CreateProduct'),
    path('update_product/<str:pd>/', views.updateProduct, name='update_product'),
    path('delete_product/<str:pd>/', views.deleteProduct, name='delete_product'),

    # Customer Create Update Delete And Order Update

    # path('create_customer/', views.createCustomer, name='create_customer'),

    path('customer_order_delete/<str:pk>/',
         views.deleteOrder, name='customer_order_delete'),
]
