from django.urls import path
from .views import showteams

urlpatterns = [
  path('', showteams)
]