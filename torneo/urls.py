from django.urls import path
from . import views
urlpatterns = [
  path('', views.showindex),
  path('form/team/done', views.createteam, name='create_team'),
  path('form/team', views.teamform, name='form_team'),
  path('list/teams', views.listarteams, name='list_team'),
  path('list/teams/delete/<int:equipo_id>', views.deleteteam, name='delete_team'),
  path('list/teams/player/form/<int:equipo_id>', views.createplayer, name='create_player'),
  #"""path('list/teams/staff/form/<int:equipo_id>/', views.staffform, name='staff_form'),
  #path('', views.createstaff, name='create_staff'), """
]
