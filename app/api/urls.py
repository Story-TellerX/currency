from django.urls import path
from rest_framework import routers
from api.views import RateViewSets, BankVListView, RateTypeChoicesView, ContactUsViewSets

router = routers.DefaultRouter()
router.register(r'rates', RateViewSets, basename='rate')
# router.register(r'banks', BankVListView, basename='bank')
router.register(r'contactuss', ContactUsViewSets, basename='contactus')

# urlpatterns = router.urls
urlpatterns = [
    path('choices/currency/types/', RateTypeChoicesView.as_view(), name='choices-currency-types'),
    path('banks/', BankVListView.as_view(), name='banks'),
]
urlpatterns += router.urls
