from django.urls import path
from rest_framework import routers
from api.views import RateViewSets, BankViewSets, RateTypeChoicesView

router = routers.DefaultRouter()
router.register(r'rates', RateViewSets, basename='rate')
router.register(r'banks', BankViewSets, basename='bank')

urlpatterns = [
    path('choices/currency/types/', RateTypeChoicesView.as_view(), name='choices-currency-types'),
]
# urlpatterns = router.urls
urlpatterns += router.urls
