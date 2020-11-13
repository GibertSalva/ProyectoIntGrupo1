from django.shortcuts import render, redirect
from.models import *
from .forms import UserRegisterForm, PropiedadForm
from django.contrib import messages


# Create your views here.
def homeview(request):
    propiedades = Propiedad.objects.all()
    imagenes = []#Array donde voy a guardar las imagenes

    for pro in propiedades: #Itero los libros
        imagen = Imagen.objects.filter(propiedad=pro).first() #Geteo la primera imagen que corresponda a ese libro
        imagenes.append(imagen.foto) #Agrego su nombre
    return render(request, "Inmobibliaria/home.html",{'propiedades':propiedades, 'imagenes':imagenes})

def propiedadview(request,id):
    propiedad = Propiedad.objects.get(id = id)
    imagenesLibro = Imagen.objects.filter(propiedad = propiedad)
    indiceEnCarusel = ["#one", "#two", "#three"] #El carusel necesita esos datos en el href para funcionar
    return render(request,"Inmobibliaria/propiedad.html",{"propiedad":propiedad, "imagenes": imagenesLibro,"indiceEnCarusel":indiceEnCarusel,"host": request.get_host()})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado')
            return redirect('/')  
    else:
        form = UserRegisterForm()
    context = {'form':form}
    return render(request,"Inmobibliaria/register.html",context)


def formularioview(request):
    data = {
        'form':PropiedadForm()
    }
        
    return render(request,"Inmobibliaria/formulario.html",data)