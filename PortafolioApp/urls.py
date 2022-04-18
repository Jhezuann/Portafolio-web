from django.urls import path

from PortafolioApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('perfil/', views.perfil, name="perfil"),
    path('contactame/', views.contactame, name="contactame"),
    path('acerca_de/', views.acerca_de, name="acerca_de"),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)