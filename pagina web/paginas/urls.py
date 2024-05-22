from django.urls import path
from .views import VistaPaginaInicial, VistaPaginaAcercaDe

urlpatterns = [
    path('', VistaPaginaInicial.as_view(), name = 'pagina_inicio'),
    path('acerca de/', VistaPaginaAcercaDe.as_view(), name = 'acerca_de'),
]
