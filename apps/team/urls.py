from django.urls import path
from rest_framework.routers import  DefaultRouter

from apps.team import views 

router = DefaultRouter()
router.register("team", views.TeamAPI , basename="team_api")

urlpatterns = [
    
]

urlpatterns += router.urls
