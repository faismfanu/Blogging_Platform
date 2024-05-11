from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from .serializers import UserSerializer, LoginSerializer
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from django.contrib import auth
import jwt

class RegisterView(GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request):
        try:
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            return Response({'detail': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class LoginView(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        try:
            data = request.data
            username = data.get('username')
            password = data.get('password')
            user = auth.authenticate(username=username,password=password)

            if user:
                auth_token = jwt.encode({'username': user.username}, settings.JWT_SECRET_KEY)    

                serializer = UserSerializer(user)

                data = {'user': serializer.data, 'token': auth_token}

                return Response(data, status=status.HTTP_200_OK)
            
            return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        
        except Exception as e:
            return Response({'detail': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)