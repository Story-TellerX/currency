from django.urls import path, re_path
# from django.views.decorators.cache import cache_page
from rest_framework import routers
from api.v1.views import RateViewSets, BankVListView, RateTypeChoicesView, ContactUsViewSets, BankVDetailsView
# LatestRates
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()
router.register(r'rates', RateViewSets, basename='rate')
# router.register(r'banks', BankVListView, basename='bank')
router.register(r'contactuss', ContactUsViewSets, basename='contactus')

# urlpatterns = router.urls
urlpatterns = [
    path('choices/currency/types/', RateTypeChoicesView.as_view(), name='choices-currency-types'),
    # path('rates/latest/', (cache_page(60 * 60 * 8))(LatestRates.as_view()), name='rates-latest'),
    path('banks/', BankVListView.as_view(), name='banks'),
    path('banks/details/<int:pk>/', BankVDetailsView.as_view(), name='bank-details'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
urlpatterns += router.urls
