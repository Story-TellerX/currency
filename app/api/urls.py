from rest_framework import routers
from api.views import RateViewSets, BankViewSets

router = routers.DefaultRouter()
router.register(r'rates', RateViewSets, basename='rate')
router.register(r'banks', BankViewSets, basename='bank')

urlpatterns = router.urls
