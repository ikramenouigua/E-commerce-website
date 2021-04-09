import django_filters 
from .models import Productt

class ProductFilter(django_filters.FuilterSet):
    class Meta:
        model =Productt
        fields='name,category'