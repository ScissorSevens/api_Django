from django.shortcuts import get_object_or_404, render
from rest_framework import  status, generics 
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .models import Persona,Tarea
from .serializers import PersonaSerializer,TareaSerializer# Create your views here.

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
