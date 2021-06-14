"""settings URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from currency.views import (
    hello_world, gen_password,
    rate_list, rate_details, rate_create, rate_update, rate_delete,
    contactus_list, contactus_details, contactus_create,
    bank_list, bank_details, bank_create, bank_update, bank_delete,
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('gen-pass/', gen_password),

    path('hello/', hello_world),

    path('currency/rate/list/', rate_list),

    path('currency/rate/details/<int:pk>/', rate_details),

    path('currency/contactus/list/', contactus_list),

    path('currency/contactus/details/<int:pk>/', contactus_details),

    path('currency/bank/list/', bank_list),

    path('currency/bank/details/<int:pk>/', bank_details),

    path('currency/rate/create/', rate_create),

    path('currency/rate/update/<int:pk>/', rate_update),

    path('currency/rate/delete/<int:pk>/', rate_delete),

    path('currency/bank/create/', bank_create),

    path('currency/bank/update/<int:pk>/', bank_update),

    path('currency/bank/delete/<int:pk>/', bank_delete),

    path('currency/contactus/create/', contactus_create),
]
