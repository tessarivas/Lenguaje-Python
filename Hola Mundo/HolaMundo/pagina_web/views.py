from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.

def vistaPagInicio(solicitud):
    return HttpResponse('Hola Mundo!')