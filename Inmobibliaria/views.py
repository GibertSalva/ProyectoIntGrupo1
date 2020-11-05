from django.shortcuts import render, redirect
from.models import *
from .forms import UserRegisterForm
from django.contrib import messages


# Create your views here.
def homeview(request):
    propiedad = Propiedad.objects.all()
    return render(request, "Inmobibliaria/home.html",{'propiedad':propiedad})

def propiedadview(request,id):
    propiedad = Propiedad.objects.get(id = id)
    return render(request,"Inmobibliaria/propiedad.html",{"propiedad":propiedad})  

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