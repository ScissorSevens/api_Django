from django.urls import path
from .views import (
    PersonaList, PersonaByDocumento, ActualizarPersona,BorrarPersonaPorDocumento
)

urlpatterns = [
    # Personas
    path('personas/', PersonaList.as_view(), name='persona-list'),
    path('personas/crear/', PersonaList.as_view(), name='persona-crear'),
    path('personas/actualizar/<int:pk>/', ActualizarPersona.as_view(), name='persona-actualizar'),
    path('personas/documento/<str:documento>/', PersonaByDocumento.as_view(), name='persona-por-documento'),
     path('personas/<str:documento>/eliminar/', BorrarPersonaPorDocumento.as_view(), name='eliminar-persona-por-documento'),
]
