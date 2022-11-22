from django.shortcuts import render, redirect
from .models import Equipos

# Create your views here.
def showteams(request):
  return render(request,'index.html')

def teamform(request):
  return render(request, 'team_form.html')

def createteam(request):
  equipo = Equipos(nombre=request.POST['nombre'], abreviatura=request.POST["abreviatura"], aniofundacion=request.POST["aniofundacion"])
  equipo.save()
  return redirect("/")


