from django.forms import ModelForm
from .models import Order, Product, Customer

# Create your Form here.


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class CreateCustomer(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
