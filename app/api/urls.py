from rest_framework import routers
from api.views import RateViewSets

router = routers.DefaultRouter()
router.register(r'rates', RateViewSets, basename='rate')

urlpatterns = router.urls
