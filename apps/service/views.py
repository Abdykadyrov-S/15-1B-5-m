from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser

from .models import *
from .serializers import *
from .permissions import IsAdminOrReadOnly

# Create your views here.

class ServiceAPICreate(ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

class ServiceAPIUpdate(UpdateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = (IsAdminOrReadOnly, )


class ServiceAPIDestroy(DestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = (IsAdminUser, )