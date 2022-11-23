from django.urls import path
from . import views
urlpatterns = [
  path('', views.showteams),
  path('form/team/done', views.createteam, name='create_team'),
  path('form/team', views.teamform, name='form_team'),
  path('delete <int:team_id>',views.deleteteam, name='delete_team'),
  path('list/teams', views.listarteams, name='list_team')
]