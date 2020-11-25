from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from.import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('', views.homeview, name = "home"),
    path("propiedad/<str:id>", views.propiedadview),
    path("register/", views.register),
    path("login/", LoginView.as_view(template_name = 'Inmobibliaria/login.html')),
    path("logout/", LogoutView.as_view(template_name = 'Inmobibliaria/logout.html')),
    path("formulario/", views.formularioview, name = "add_propiedad"),
    path("aboutas/",views.about_as),
    path("perfil/<str:usuario>",views.perfil, name = "perfil"),
    path("eliminar-propiedad/<id>/",views.eliminar_propiedad, name = 'eliminar_propiedad')
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 