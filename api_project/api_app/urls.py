from django.urls import path
from .views import (
    PersonaList, CrearPersona,PersonaByDocumento, ActualizarPersona,BorrarPersonaPorDocumento,TareaList,CrearTarea,ActualizarTarea,BorrarTarea,TareasPorFecha,TareasPorRangoFecha,TareasPorPersona
)

urlpatterns = [
    # Personas
    path('personas/', PersonaList.as_view(), name='persona-list'),
    path('personas/crear/', CrearPersona.as_view(), name='persona-crear'),
    path('personas/actualizar/<int:pk>/', ActualizarPersona.as_view(), name='persona-actualizar'),
    path('personas/documento/<str:documento>/', PersonaByDocumento.as_view(), name='persona-por-documento'),
     path('personas/<str:documento>/eliminar/', BorrarPersonaPorDocumento.as_view(), name='eliminar-persona-por-documento'),
    # Tareas
    path('tareas/', TareaList.as_view(), name='tarea-list'),
     path('tareas/crear/', CrearTarea.as_view(), name='crear-tarea'),
    path('tareas/<int:pk>/actualizar/', ActualizarTarea.as_view(), name='actualizar-tarea'),
    path('tareas/<int:pk>/eliminar/', BorrarTarea.as_view(), name='eliminar-tarea'),

    # Filtros
    path('tareas/fecha/<str:fecha>/', TareasPorFecha.as_view(), name='tareas-por-fecha'),
    path('tareas/rango/<str:fecha_inicio>/<str:fecha_fin>/', TareasPorRangoFecha.as_view(), name='tareas-por-rango'),
    path('tareas/persona/<int:persona_id>/', TareasPorPersona.as_view(), name='tareas-por-persona'),
]
