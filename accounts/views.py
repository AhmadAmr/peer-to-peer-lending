from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView 
from .serializers import CustomUserSerializer
from rest_framework import permissions,status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.tokens import RefreshToken
from .models import CustomUser
from django.http import JsonResponse
from rest_framework.generics import UpdateAPIView
from rest_framework import mixins, permissions, generics

# Create your views here.

class CreateCustomUser(APIView):
    permission_classes=(permissions.AllowAny ,)

    def post(self,request ,format='json'):
        serializer = CustomUserSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json_obj = serializer.data
                return Response(json_obj, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)