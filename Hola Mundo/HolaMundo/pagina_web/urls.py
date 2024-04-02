from django.urls import path
from .views import vistaPagInicio

urlpatterns = [
    path('', vistaPagInicio, name ='PaginaInicio')
]
