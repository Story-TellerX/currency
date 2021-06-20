from django.contrib import admin
from rangefilter.filters import DateRangeFilter, DateTimeRangeFilter

from currency.models import Rate


class RateAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'source',
        'type_curr',
        'buy',
        'sale',
        'created',
    )
    list_filter = (
        ('created_at', DateRangeFilter),
        ('updated_at', DateTimeRangeFilter),
        'type_curr',
        'source',
        'created',
    )


admin.site.register(Rate, RateAdmin)
