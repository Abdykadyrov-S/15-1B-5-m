from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import *

urlpatterns = [
    path('', UserAPI.as_view(), name='api_users'),
    path('register/', UserRegisterAPI.as_view(), name="api_user_register"),
    path('login/', TokenObtainPairView.as_view(), name='api_user_login'),
    path('refresh/', TokenRefreshView.as_view(), name='api_user_refresh')
]
