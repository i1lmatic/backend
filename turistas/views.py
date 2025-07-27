from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .models import Turista
from .serializers import RegistroTuristaSerializer, TuristaSerializer

class RegistroTuristaView(APIView):
    def post(self, request):
        serializer = RegistroTuristaSerializer(data=request.data)
        if serializer.is_valid():
            turista = serializer.save()
            token, created = Token.objects.get_or_create(user=turista)
            return Response({'token': token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginTuristaView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        turista = authenticate(email=email, password=password)
        if turista:
            token, created = Token.objects.get_or_create(user=turista)
            return Response({'token': token.key})
        return Response({'error': 'Credenciales inválidas'}, status=status.HTTP_401_UNAUTHORIZED)

class PerfilTuristaView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        serializer = TuristaSerializer(request.user)
        return Response(serializer.data)
