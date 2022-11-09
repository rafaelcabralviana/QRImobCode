import django_filters

from .models import Product




class ListingFilter(django_filters.FilterSet):
    
    class Meta:
        model = Product
        fields = {'setor': ['icontains']}
