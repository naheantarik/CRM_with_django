import django_filters
from .models import *


# Create Filters Here

class OrderFilters(django_filters.FilterSet):
    class Meta:
        model = Order
        fields = '__all__'
