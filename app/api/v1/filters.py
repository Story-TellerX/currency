from django_filters import rest_framework as filters

from currency.models import Rate, ContactUs


class RateFilter(filters.FilterSet):

    class Meta:
        model = Rate
        # fields = ['category', 'in_stock', 'min_price', 'max_price']
        fields = {
            'buy': ('lt', 'lte', 'gt', 'gte', 'exact'),
            'sale': ('lt', 'lte', 'gt', 'gte', 'exact'),
            'type_curr': ('in',),
            'created': ('date', 'lte', 'gte'),
        }


class ContactUsFilter(filters.FilterSet):

    class Meta:
        model = ContactUs
        fields = {
            'email_from': ('lt', 'lte', 'gt', 'gte', 'exact'),
            'subject': ('lt', 'lte', 'gt', 'gte', 'exact'),
            'message': ('lt', 'lte', 'gt', 'gte', 'exact'),
            'created': ('lte', 'gte', 'date'),
        }
