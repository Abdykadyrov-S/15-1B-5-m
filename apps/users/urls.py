from django.urls import path

from .views import *

urlpatterns = [
    path('', UserAPI.as_view(), name='api_users'),
    path('register/', UserRegisterAPI.as_view(), name="api_user_register")
]
