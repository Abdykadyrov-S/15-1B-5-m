from django.shortcuts import render

from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from .models import Team
from .serialiizers import TeamSerializer

# Create your views here.
class TeamAPI(GenericViewSet,
              mixins.ListModelMixin,
              mixins.CreateModelMixin,
              mixins.RetrieveModelMixin,
              mixins.UpdateModelMixin,
              mixins.DestroyModelMixin,
              ):
    
    queryset = Team.objects.all() 
    serializer_class = TeamSerializer