from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from .models import Empresa
from .serializers import EmpresaRegistroSerializer, LoginSerializer, EmpresaSerializer
from rest_framework.permissions import IsAuthenticated

class RegistroEmpresaView(APIView):
    def post(self, request):
        serializer = EmpresaRegistroSerializer(data=request.data)
        if serializer.is_valid():
            empresa = serializer.save()
            token, _ = Token.objects.get_or_create(user=empresa)
            return Response({'token': token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginEmpresaView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PerfilEmpresaView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = EmpresaSerializer(request.user)
        return Response(serializer.data)
