from django.urls import path
from . import views
urlpatterns = [
  path('', views.showteams),
  path('create', views.createteam, name='create_team')
]