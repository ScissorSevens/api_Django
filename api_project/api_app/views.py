from django.shortcuts import get_object_or_404, render
from rest_framework import  status, generics 
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .models import Persona,Tarea
from .serializers import PersonaSerializer,TareaSerializer# Create your views here.


#Vistas de personas
class PersonaList(generics.ListCreateAPIView):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer

    def get(self, request):
       personas = Persona.objects.all()
       serializer = self.get_serializer(personas, many=True)
       if not personas:
           raise NotFound("No se encontraron personas.")
       return Response({'success':True,'detail':'listado de personas','data':serializer.data}, status=status.HTTP_200_OK)
    

#crear personas

class CrearPersona(generics.CreateAPIView):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer

    def post(self, request):
      serializers= PersonaSerializer(data=request.data)
      serializers.is_valid(raise_exception=True)
      serializers.save()
      return Response({'success':True,'detail':'Persona creada con éxito','data':serializers.data}, status=status.HTTP_201_CREATED)

class ActualizarPersona(generics.UpdateAPIView):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer

    def put(self, request, pk):
        persona = get_object_or_404(Persona, pk=pk)
        email = request.data.get('email', None)

        # Validar email duplicado
        if email and email != persona.email:
            if Persona.objects.filter(email=email).exclude(pk=pk).exists():
                return Response(
                    {'success': False, 'detail': 'El email ya está en uso por otra persona'},
                    status=status.HTTP_400_BAD_REQUEST
                )

        # Serializar y guardar actualización
        serializer = PersonaSerializer(persona, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {'success': True, 'detail': 'Persona actualizada con éxito', 'data': serializer.data},
            status=status.HTTP_200_OK
        )

class PersonaByDocumento(generics.RetrieveAPIView):
    serializer_class = PersonaSerializer

    def get(self, request, documento):
       persona=Persona.objects.filter(documento=documento).first()
       if not persona:
           return Response({'success':False,'detail':'Persona no encontrada'}, status=status.HTTP_404_NOT_FOUND)
       serializer =PersonaSerializer(persona)
       return Response({'success':True,'detail':'Persona encontrada','data':serializer.data}, status=status.HTTP_200_OK)
    
class BorrarPersonaPorDocumento(generics.DestroyAPIView):
    serializer_class = PersonaSerializer

    def delete(self, request, documento):
        persona = Persona.objects.filter(documento=documento).first()
        if not persona:
            return Response(
                {
                    'success': False,
                    'detail': 'Persona no encontrada'
                },
                status=status.HTTP_404_NOT_FOUND
            )
        
        persona.delete()
        return Response(
            {
                'success': True,
                'detail': f'Persona con documento {documento} eliminada con éxito'
            },
            status=status.HTTP_200_OK
        )

#vistas de tareas 

# Listar todas las tareas
class TareaList(generics.ListAPIView):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer

    def get(self, request):
        tareas = Tarea.objects.all()
        if not tareas:
            raise NotFound("No se encontraron tareas.")
        serializer = self.get_serializer(tareas, many=True)
        return Response(
            {'success': True, 'detail': 'Listado de tareas', 'data': serializer.data},
            status=status.HTTP_200_OK
        )
# Crear tarea
class CrearTarea(generics.CreateAPIView):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {'success': True, 'detail': 'Tarea creada con éxito', 'data': serializer.data},
            status=status.HTTP_201_CREATED
        )


# Actualizar tarea
class ActualizarTarea(generics.UpdateAPIView):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer

    def put(self, request, pk):
        tarea = get_object_or_404(Tarea, pk=pk)
        serializer = self.get_serializer(tarea, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {'success': True, 'detail': 'Tarea actualizada con éxito', 'data': serializer.data},
            status=status.HTTP_200_OK
        )


# Borrar tarea
class BorrarTarea(generics.DestroyAPIView):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer

    def delete(self, request, pk):
        tarea = get_object_or_404(Tarea, pk=pk)
        tarea.delete()
        return Response(
            {'success': True, 'detail': 'Tarea eliminada con éxito'},
            status=status.HTTP_200_OK
        )


# ---------------- FILTROS ----------------

# Filtrar tareas por fecha límite exacta
class TareasPorFecha(generics.ListAPIView):
    serializer_class = TareaSerializer

    def get(self, request, fecha):
        tareas = Tarea.objects.filter(fecha_limite=fecha)
        if not tareas:
            return Response(
                {'success': False, 'detail': 'No se encontraron tareas para esta fecha'},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = self.get_serializer(tareas, many=True)
        return Response(
            {'success': True, 'detail': f'Tareas con fecha límite {fecha}', 'data': serializer.data},
            status=status.HTTP_200_OK
        )


# Filtrar tareas por rango de fechas
class TareasPorRangoFecha(generics.ListAPIView):
    serializer_class = TareaSerializer

    def get(self, request, fecha_inicio, fecha_fin):
        tareas = Tarea.objects.filter(fecha_limite__range=[fecha_inicio, fecha_fin])
        if not tareas:
            return Response(
                {'success': False, 'detail': 'No se encontraron tareas en este rango de fechas'},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = self.get_serializer(tareas, many=True)
        return Response(
            {'success': True, 'detail': f'Tareas entre {fecha_inicio} y {fecha_fin}', 'data': serializer.data},
            status=status.HTTP_200_OK
        )


# Filtrar tareas por persona
class TareasPorPersona(generics.ListAPIView):
    serializer_class = TareaSerializer

    def get(self, request, persona_id):
        tareas = Tarea.objects.filter(persona_id=persona_id)
        if not tareas:
            return Response(
                {'success': False, 'detail': 'No se encontraron tareas para esta persona'},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = self.get_serializer(tareas, many=True)
        return Response(
            {'success': True, 'detail': f'Tareas de la persona con ID {persona_id}', 'data': serializer.data},
            status=status.HTTP_200_OK
        )