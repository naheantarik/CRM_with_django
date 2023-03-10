from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


from .models import Order, Product, Customer


# Create your Form here.

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


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


class CreateCustomer(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
