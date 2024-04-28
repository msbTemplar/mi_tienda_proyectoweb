from django.shortcuts import render

# servicios es mi app 
from servicios.models import Servicio

# Create your views here.


def servicios(request):
    
    servicios=Servicio.objects.all()

    
    #return HttpResponse("Servicios")
    return render(request, "servicios/servicios.html", {"servicios": servicios})