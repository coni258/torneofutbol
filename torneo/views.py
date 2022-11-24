from django.shortcuts import render, redirect
from .models import Equipos
from .models import Jugadores
from .models import Staff

# Create your views here.
def showindex(request):
  return render(request,'index.html')

def teamform(request):
  return render(request, 'team_form.html')

def playerform(request, equipo_id):
  return render(request, 'player_form.html')

def listarteams(request):
  equipos = Equipos.objects.all()
  return render(request, 'list_teams.html', {'Equipos': equipos})

def createteam(request):
  equipo = Equipos(nombre=request.POST['nombre'], abreviatura=request.POST['abreviatura'], aniofundacion=request.POST['aniofundacion'])
  equipo.save()
  return redirect("/")

def deleteteam(request, equipo_id):
  equipo = Equipos.objects.get(id=equipo_id)
  equipo.delete()
  return redirect("/list/teams")


def createplayer(request, equipo_id):
  jugador = Jugadores(num_pasaporte=request.POST['num_pasaporte'], nombre=request.POST['nombre'], nacionalidad=request.POST['nacionalidad'], edad=request.POST['edad'], posicion=request.POST['posicion'], abr_posicion=request.POST['abr_posicion'], cargo=request.POST['cargo'], abr_cargo=request.POST['abr_cargo'],num_dorsal=request.POST['num_dorsal'], equipo_id = equipo_id)
  jugador.save()
  return redirect ("/list/teams")

"""def listarplayer(request):
  jugadores = Jugadores.objects.all()
  return render(request, 'list_jugadores.html', {'Jugadores': jugadores})"""


"""
def deleteplayer(request,jugador_id):
  jugadores=Jugadores.objects.get(id=jugador_id)
  jugadores.delete()
  return redirect("player/list")

def createstaff(request):
  staff =Staff(num_pasaporte=request.POST['num_pasaporte'],nombre=request.POST['nombre'],nacionalidad=request.POST['nacionalidad'],edad=request.POST['edad'],cargo=request.POST['cargo'],abr_cargo=request.POST['abr_cargo'])
  staff.save()
  return redirect ("/")

def deletestaff(request,staff_id):
  staff=Staff.objects.get(id=staff_id)
  staff.delete()
  return redirect ("staff/list")


def editplayer(request, jugador_id):
  jugador = Jugadores.objects.filter(id=jugador_id).first()
  busca = Jugadores(instance=jugador)
  return render(request)


"""