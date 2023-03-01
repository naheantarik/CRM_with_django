from django.forms import ModelForm
from .models import Order
from .models import Product

# Create your Form here.


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
