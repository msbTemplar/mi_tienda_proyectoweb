from django.shortcuts import render, HttpResponse

from carro.carro import Carro




# Create your views here.

def home(request):
   
   carro=Carro(request)
   
   # return HttpResponse("Home")
   return render(request, "ProyectoWebApp/home.html")















