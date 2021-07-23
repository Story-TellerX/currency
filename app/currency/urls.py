from django.urls import path
from currency.views import (
    GenPassword, HelloWorld,
    ContactusListView, ContactusDetailView, CreateContactUs,
    BankListView, BankCreateView, BankDetailView, BankUpdateView, BankDeleteView,
    RateListView, RateCreateView, RateDetailView, RateUpdateView, RateDeleteView, RateListApi,
)

app_name = 'currency'

urlpatterns = [
    path('gen-pass/', GenPassword.as_view(), name='gen-pass'),
    path('hello/', HelloWorld.as_view(), name='hello-world'),

    path('api/rates/', RateListApi.as_view()),

    path('rate/list/', RateListView.as_view(), name="rate-list"),
    path('rate/details/<int:pk>/', RateDetailView.as_view(), name="rate-details"),
    path('rate/create/', RateCreateView.as_view(), name="rate-create"),
    path('rate/update/<int:pk>/', RateUpdateView.as_view(), name="rate-update"),
    path('rate/delete/<int:pk>/', RateDeleteView.as_view(), name="rate-delete"),

    path('bank/list/', BankListView.as_view(), name="bank-list"),
    path('bank/details/<int:pk>/', BankDetailView.as_view(), name="bank-details"),
    path('bank/create/', BankCreateView.as_view(), name="bank-create"),
    path('bank/update/<int:pk>/', BankUpdateView.as_view(), name="bank-update"),
    path('bank/delete/<int:pk>/', BankDeleteView.as_view(), name="bank-delete"),

    path('contactus/list/', ContactusListView.as_view(), name="contactus-list"),
    path('contactus/details/<int:pk>/', ContactusDetailView.as_view(), name="contactus-details"),
    path('contact-us/create/', CreateContactUs.as_view(), name="contact-us-create"),
]
