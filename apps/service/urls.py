from django.urls import path

from .views import *

urlpatterns = [
    path('', ServiceAPICreate.as_view(), name='Service_create_api'),
    path('update/<int:pk>/', ServiceAPIUpdate.as_view(), name='Service_update_api'),
    path('destroy/<int:pk>/', ServiceAPIDestroy.as_view(), name='Service_destroy_api'),
]
