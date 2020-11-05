from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from.import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('', homeview, name = "home"),
    path("propiedad/<str:id>", propiedadview),
    path("register/", views.register),
    path("login/", LoginView.as_view(template_name = 'Inmobibliaria/login.html')),
    path("logout/", LogoutView.as_view(template_name = 'Inmobibliaria/logout.html')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 