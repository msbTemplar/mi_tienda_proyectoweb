from django.shortcuts import render, redirect

from .forms import FormularioContacto

from django.core.mail import EmailMessage

from django.core.mail import send_mail

# Create your views here.

def contacto(request):

    formulario_contacto=FormularioContacto()

    if  request.method=="POST":
        formulario_contacto=FormularioContacto(data=request.POST)

        if formulario_contacto.is_valid():
            nombre=request.POST.get("nombre")
            email=request.POST.get("email")
            contenido=request.POST.get("contenido")
            auth_password="anbc ictn simy cfrq"
            
            """
            email=EmailMessage("Mensaje desde App Django",
                               "El usuario con nombre {} con la dirección {} escribe lo siguiente:\n\n {}".format(nombre,email,contenido),
                               "msb.duck@gmail.com",["msb.duck@gmail.com"],reply_to=[email])
            """
            
             #email.send()
            try:  
                send_mail("Mensaje desde App Django","El usuario con nombre {} con la dirección {} escribe lo siguiente:\n\n {}".format(nombre,email,contenido),
                      "msb.duck@gmail.com",["msebti2@gmail.com","msb.tesla@gmail.com"],fail_silently=False, auth_password=auth_password)   
          
                
                            
                return redirect("/contacto/?valido")
            except:
                return redirect("/contacto/?novalido")
        
   
    
   # return HttpResponse("Contacto")
    return render(request, "contacto/contacto.html", {'miFormulario':formulario_contacto})



