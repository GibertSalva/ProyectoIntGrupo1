from django.shortcuts import render
from.models import *

# Create your views here.
def homeview(request):
    propiedad = Propiedad.objects.all()
    return render(request, "Inmobibliaria/home.html",{'propiedad':propiedad})

def propiedadview(request,id):
    propiedad = Propiedad.objects.get(id = id)
    return render(request,"Inmobibliaria/propiedad.html",{"propiedad":propiedad}) 