from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from .models import *
from .serializers import *

# Create your views here.
class NewsAPIView(ListAPIView):
    queryset = News.objects.all() # SELECT * FROM 
    serializer_class = NewsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'description']

class NewsAPICreate(CreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (IsAuthenticated, )

class NewsAPIRetrieve(RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsDetailSerializer

class NewsAPIUpdate(UpdateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsDetailSerializer

class NewsAPIDestroy(DestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsDetailSerializer

    