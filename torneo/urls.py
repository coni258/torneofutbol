from django.urls import path
from . import views
urlpatterns = [
  path('', views.showindex),
  path('form/team/done', views.createteam, name='create_team'),
  path('form/team', views.teamform, name='form_team'),
  path('list/teams', views.listarteams, name='list_team'),
  path('list/teams/delete/<int:equipo_id>/', views.deleteteam, name='delete_team'),
  path('list/teams/player/form/<int:equipo_id>/', views.playerform, name='player_form'),
  path('', views.createplayer, name='create_player'),
  
]
