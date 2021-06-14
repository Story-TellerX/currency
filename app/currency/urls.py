from django.urls import path
from currency.views import (
    hello_world, gen_password,
    rate_list, rate_details, rate_create, rate_update, rate_delete,
    contactus_list, contactus_details, contactus_create,
    bank_list, bank_details, bank_create, bank_update, bank_delete,
)

app_name = 'currency'

urlpatterns = [
    path('gen-pass/', gen_password),
    path('hello/', hello_world),
    path('rate/list/', rate_list, name="rate-list"),
    path('rate/details/<int:pk>/', rate_details, name="rate-details"),
    path('rate/create/', rate_create, name="rate-create"),
    path('rate/update/<int:pk>/', rate_update, name="rate-update"),
    path('rate/delete/<int:pk>/', rate_delete, name="rate-delete"),
    path('bank/list/', bank_list, name="bank-list"),
    path('bank/details/<int:pk>/', bank_details, name="bank-details"),
    path('bank/create/', bank_create, name="bank-create"),
    path('bank/update/<int:pk>/', bank_update, name="bank-update"),
    path('bank/delete/<int:pk>/', bank_delete, name="bank-delete"),
    path('contactus/list/', contactus_list, name="contactus-list"),
    path('contactus/details/<int:pk>/', contactus_details, name="contactus-details"),
    path('contactus/create/', contactus_create, name="contactus-create"),
]
