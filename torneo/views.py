from django.shortcuts import render

# Create your views here.
def showteams(request):
  return render(request,'index.html')

def create_teams(request):
  print(request.POST)