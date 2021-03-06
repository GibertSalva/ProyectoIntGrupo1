from django.shortcuts import render, redirect, get_object_or_404
from.models import *
from .forms import UserRegisterForm, PropiedadModelForm, ComentarioModelForm
from django.contrib import messages
from django.forms.models import inlineformset_factory
from django.views.generic.edit import CreateView, UpdateView
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail
from django.conf import settings




# Create your views here.
def homeview(request):
    propiedades = Propiedad.objects.all().order_by('-fecha')
    imagenes = []#Array donde voy a guardar las imagenes

    for pro in propiedades: #Itero los libros
        imagen = Imagen.objects.filter(propiedad=pro).first() #Geteo la primera imagen que corresponda a ese libro
        imagenes.append(imagen.foto) #Agrego su nombre
    return render(request, "Inmobibliaria/home.html",{'propiedades':propiedades, 'imagenes':imagenes})

def about_as(request):
    return render(request,'Inmobibliaria/aboutas.html')

def perfil(request, usuario):
    user = User.objects.get(username=usuario)
    propiedades=Propiedad.objects.filter(usuario=user)

    data = {
        'propiedades':propiedades,
        'usuario':user
    }

    return render(request,'Inmobibliaria/perfil.html',data)

def eliminar_propiedad(request,id):
    propiedad = get_object_or_404(Propiedad, id=id)
    propiedad.delete()
    messages.success(request, f'Propiedad {propiedad.titulo} eliminada')
    return redirect('/')

def propiedadview(request,id):
    propiedad = Propiedad.objects.get(id = id)
    imagenesLibro = Imagen.objects.filter(propiedad = propiedad)
    indiceEnCarusel = ["#one", "#two", "#three"] #El carusel necesita esos datos en el href para funcionar

    if request.method == 'POST':
        form = ComentarioModelForm(request.POST)
        current_user = get_object_or_404(User, pk = request.user.pk)
        if form.is_valid():
            created_comentario = form.save(commit=False)
            created_comentario.user = current_user
            created_comentario.propiedad = propiedad
            if created_comentario.user != created_comentario.propiedad.usuario:
                created_comentario.save()
                subject = "Has recibido una consulta de tu propiedad " + propiedad.titulo
                message = "De: " + created_comentario.user.username + "\nCorreo: "+ created_comentario.user.email + "\n" + created_comentario.mensaje 
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [propiedad.usuario.email]
                send_mail(subject, message, email_from, recipient_list) 


                messages.success(request, f'Tu consulta ha sido enviada!')
                return redirect('/')
            
            else:
                messages.success(request, f'No puedes consultar una propiedad tuya')

            
    else:
        form = ComentarioModelForm()


    return render(request,"Inmobibliaria/propiedad.html",{"propiedad":propiedad, "imagenes": imagenesLibro,"indiceEnCarusel":indiceEnCarusel,"host": request.get_host(),"form":form})


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
        'foto',
    }
    current_user = get_object_or_404(User, pk = request.user.pk)
    propiedad = Propiedad()
    form = PropiedadModelForm(instance=propiedad)
    ImagenInlineFormSet = inlineformset_factory(Propiedad, Imagen, fields=('foto',),min_num=1)
    
    if request.method == 'POST':
        form = PropiedadModelForm(request.POST, request.FILES)
        formset = ImagenInlineFormSet(request.POST, request.FILES)
        formset = ImagenInlineFormSet(data)
           

        if form.is_valid():
            created_propiedad = form.save(commit = False)
            created_propiedad.usuario = current_user
            formset = ImagenInlineFormSet(request.POST, request.FILES, instance=created_propiedad)

        
            if formset.is_valid():
                created_propiedad.save()
                formset.save()
                return redirect ('/')
    else:
        form = PropiedadModelForm(instance=propiedad)
        formset = ImagenInlineFormSet()
        
    return render(request,"Inmobibliaria/formulario.html",{'form':form,'formset':formset})


