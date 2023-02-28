from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.


def home(request):
    customers = Customer.objects.all()
    orders = Order.objects.all()
    total_orders = orders.count()
    total_customers = customers.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context = {'orders': orders, 'customers': customers,
               'total_orders': total_orders, 'total_customers': total_customers, 'delivered': delivered, 'pending': pending}
    return render(request, 'accounts/dashboard.html', context)


def product(request):
    products = Product.objects.all()
    return render(request, 'accounts/product.html', {'products': products})


def customer(request, cng):
    customer = Customer.objects.get(id=cng)
    orders = customer.order_set.all()
    total_orders = orders.count()
    context = {'orders': orders, 'customer': customer,
               'total_orders': total_orders, }
    return render(request, 'accounts/customer.html', context)
