from django.shortcuts import render
from rest_framework.generics import *

from .models import *
from .serializers import *

# Create your views here.
class UserAPI(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserRegisterAPI(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer