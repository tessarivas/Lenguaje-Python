from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class VistaPaginaInicial(TemplateView):
    template_name = 'pagina_inicio.html'

class VistaPaginaAcercaDe(TemplateView):
    template_name = 'acerca_de.html'