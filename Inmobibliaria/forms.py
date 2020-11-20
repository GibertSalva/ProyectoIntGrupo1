from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from.models import *
from django.forms.models import inlineformset_factory
#from .models import Post

class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()
	password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
	password2 = forms.CharField(label='Confirma Contraseña', widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']
		help_texts = {k:"" for k in fields }




class UbicacionForm(forms.ModelForm):

	class Meta:
		model = Ubicacion

		fields = [
			'provincia',
		]

class PropiedadModelForm(forms.ModelForm):
	
	class Meta:
		model = Propiedad

		fields = [
			'titulo',
			'precio',
			'tipo',
			'estado',
			'ubicacion',
			'barrio',
			'calle',
			'numero',
			'habitaciones',
			'baños',
			'tamaño',
			'descripcion',
		]

class ImagenModelForm(forms.ModelForm):

	class Meta:
		model = Imagen
		fields = ['foto']


class ComentarioModelForm(forms.ModelForm):
	class Meta:
		model = Comentario
		fields = ['mensaje']









'''
ImagenInlineFormSet = inlineformset_factory(
    Propiedad, Imagen, form=ImagenForm, 
    extra=3, can_delete=True)
'''

'''
	labels = {
		'titulo':'Titulo',
		'precio':'Precio',
		'ubicacion':'Ubicación',
		'tipo':'Tipo',
		'estado':'Estado',
		'habitaciones':'Habitaciones',
		'baños':'Baños',
		'tamaño':'Tamaño',
		'descripcion':'Descripción',
	}
	widgets = {
		'titulo': forms.TextInput(),
		'precio': forms.NumberInput(),
		'ubicacion':,
		'tipo',
		'estado',
		'habitaciones',
		'baños',
		'tamaño',
		'descripcion',
	}
'''

