from django.urls import path
from accounts.views import MyProfile, SignUp, ActivateAccount

app_name = 'accounts'

urlpatterns = [
    # path('my-profile/<int:pk>/', MyProfile.as_view(), name='my-profile'),
    path('my-profile/', MyProfile.as_view(), name='my-profile'),
    path('signup/', SignUp.as_view(), name='signup'),
    # path('activate/account/<uuid:activation_key>/', ActivateAccount.as_view(), name='activate-account'),
    path('activate/account/<uuid:activation_key>/<token>/', ActivateAccount.as_view(), name='activate-account'),
]
