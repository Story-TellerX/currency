from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from rangefilter.filters import DateTimeRangeFilter, DateRangeFilter

from currency.models import Rate, Bank, ContactUs

from import_export import resources


class RateResource(resources.ModelResource):

    class Meta:
        model = Rate


class ContactUsResource(resources.ModelResource):

    class Meta:
        model = ContactUs


class RateAdmin(ImportExportModelAdmin):
    resource_class = RateResource

    list_display = (
        'id',
        'source',
        'type_curr',
        'buy',
        'sale',
        'created',
    )
    list_filter = (
        # ('created', DateRangeFilter),
        ('created', DateTimeRangeFilter),
        'type_curr',
        'source',
        'created',
    )

    search_fields = (
        'type_curr',
        'source',
    )

    readonly_fields = (
        'id',
        'buy',
        'sale',
    )


class BankAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'url',
        'number',
        'created',
    )
    list_filter = (
        ('created', DateRangeFilter),
        # ('created', DateTimeRangeFilter),
        'name',
        'number',
        'created',
    )

    search_fields = (
        'name',
        'number',
        'url',
    )

    readonly_fields = (
        'id',
        'created',
    )


class ContactUsAdmin(ImportExportModelAdmin):
    resource_class = ContactUsResource
    list_display = (
        'id',
        'email_from',
        'subject',
        'message',
        'created',
    )

    search_fields = (
        'email_from',
        'subject',
        'message',
    )

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Bank, BankAdmin)
admin.site.register(ContactUs, ContactUsAdmin)
admin.site.register(Rate, RateAdmin)
