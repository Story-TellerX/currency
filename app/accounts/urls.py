from django.urls import path
from accounts.views import MyProfile

app_name = 'accounts'

urlpatterns = [
    # path('my-profile/<int:pk>/', MyProfile.as_view(), name='my-profile'),
    path('my-profile/', MyProfile.as_view(), name='my-profile'),
]
