import django_filters
from django_filters import DateFilter
from .models import *


# Create Filters Here

class OrderFilters(django_filters.FilterSet):
    startdate = DateFilter(field_name="date_created", lookup_expr='gte')
    enddate = DateFilter(field_name="date_created", lookup_expr='lte')

    class Meta:
        model = Order
        fields = '__all__'
        exclude = ['customer', 'date_created']
