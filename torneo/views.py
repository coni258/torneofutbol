from django.shortcuts import render, redirect
from .models import Equipos
from .models import Jugadores
from .models import Staff

# Create your views here.
def showindex(request):
  return render(request,'index.html')

def teamform(request):
  return render(request, 'team_form.html')

def listarteams(request):
  equipos = Equipos.objects.all()
  return render(request, 'list_teams.html', {'Equipos': equipos})

def createteam(request):
  print("hola")
  equipo = Equipos(nombre=request.POST['nombre'], abreviatura=request.POST['abreviatura'], aniofundacion=request.POST['aniofundacion'])
  equipo.save()
  return redirect("/")

def deleteteam(equipo_id):
  equipo = Equipos.objects.get(id=equipo_id)
  equipo.delete()
  return redirect("/list/teams")

def playerform(request, equipo_id):
  return render(request, 'player_form.html', {'equipo_id': equipo_id})

def createplayer(request, equipo_id):
  jugador =Jugadores(num_pasaporte=request.POST['num_pasaporte'],nombre=request.POST['nombre'],nacionalidad=request.POST['nacionalidad'],edad=request.POST['edad'],posicion=request.POST['posicion'],abr_posicion=request.POST['abr_posicion'],num_dorsal=request.POST['num_dorsal'], equipo_id=request.POST['equipo_id'])
  jugador.save()
  return redirect ("/")


def createstaff(request):
  staff =Staff(num_pasaporte=request.POST['num_pasaporte'],nombre=request.POST['nombre'],nacionalidad=request.POST['nacionalidad'],edad=request.POST['edad'],cargo=request.POST['cargo'],abr_cargo=request.POST['abr_cargo'])
  staff.save()
  return redirect ("/")
