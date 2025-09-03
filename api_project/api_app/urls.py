from django.urls import path
from .views import (
    PersonaList, PersonaByDocumento, ActualizarPersona,
)

urlpatterns = [
    # Personas
    path('personas/', PersonaList.as_view(), name='persona-list'),
    path('personas/crear/', PersonaList.as_view(), name='persona-crear'),
    path('personas/actualizar/<int:pk>/', ActualizarPersona.as_view(), name='persona-actualizar'),
    path('personas/documento/<str:documento>/', PersonaByDocumento.as_view(), name='persona-por-documento'),
]
