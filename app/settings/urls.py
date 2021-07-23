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
import debug_toolbar
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from currency.views import IndexTemplateView
# from api.views import RateList, RateListCreate, RateDetails

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexTemplateView.as_view(), name='index'),
    path('currency/', include('currency.urls')),
    path('__debug__/', include(debug_toolbar.urls)),
    path('auth/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('api/', include('api.urls')),

    # path('rates/', RateList.as_view()),
    # path('ratescreate/', RateListCreate.as_view()),
    # path('ratedetails/<int:pk>', RateDetails.as_view()),
]

urlpatterns.extend(static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))
urlpatterns.extend(static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
