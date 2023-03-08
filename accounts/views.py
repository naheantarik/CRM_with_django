from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .form import OrderForm, ProductForm, CreateCustomer
from .filters import OrderFilters, ProductFielters
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your views here.


def registerPage(request):
    form = UserCreationForm()
    context = {'form': form}
    return render(request, 'accounts/register.html', context)


def login(request):
    form = User()
    context = {'form': form}
    return render(request, 'accounts/login.html', context)


def home(request):
    customers = Customer.objects.all()
    orders = Order.objects.all()
    # productFilters = ProductFielters(request.GET, queryset=orders)
    # orders = productFilters.qs
    total_orders = orders.count()
    total_customers = customers.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context = {'orders': orders,
               'total_orders': total_orders, 'total_customers': total_customers, 'delivered': delivered, 'pending': pending}
    return render(request, 'accounts/dashboard.html', context)


def product(request):
    products = Product.objects.all()
    return render(request, 'accounts/product.html', {'products': products})


def customerPage(request):
    customers = Customer.objects.all()
    context = {'customers': customers}
    return render(request, 'accounts/customer_page.html', context)


def customer(request, cng):
    customer = Customer.objects.get(id=cng)
    orders = customer.order_set.all()
    myFilters = OrderFilters(request.GET, queryset=orders)
    orders = myFilters.qs
    total_orders = orders.count()
    context = {'orders': orders, 'customer': customer,
               'total_orders': total_orders, 'myFilters': myFilters}
    return render(request, 'accounts/customer.html', context)


def createOrder(request, pk):
    customer = Customer.objects.get(id=pk)
    form = OrderForm(initial={'customer': customer})
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'accounts/order_form.html', context)


def update_order(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'accounts/order_form.html', context)


def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)

    if request.method == 'POST':
        order.delete()
        return redirect('/')

    context = {'item': order}
    return render(request, 'accounts/delete.html', context)


def createProduct(request):
    form = ProductForm()

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/product')

    context = {'form': form}
    return render(request, 'accounts/product_create.html', context)


def updateProduct(request, pd):
    product = Product.objects.get(id=pd)
    form = ProductForm(instance=product)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('/product')

    context = {'form': form}
    return render(request, 'accounts/product_create.html', context)


def deleteProduct(request, pd):
    product = Product.objects.get(id=pd)
    if request.method == 'POST':
        product.delete()
        return redirect('/product')

    context = {'item': product}
    return render(request, 'accounts/product_delete.html', context)


# Customer Section

def createCustomer(request):
    form = CreateCustomer()
    if request.method == 'POST':
        form = CreateCustomer(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/customer_page')
    context = {'form': form}
    return render(request, 'accounts/create_customer.html', context)


def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    # customers = Customer.objects.get(id=pk)

    if request.method == 'POST':
        order.delete()
        return redirect('/')

    context = {'item': order}
    return render(request, 'accounts/delete.html', context)
