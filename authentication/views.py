import jwt

from django.shortcuts import render
from django.conf import settings
from django.contrib import auth

from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import UserSerializer, LoginSerializer
from .backends import JWTAuthentication

# Create your views here.


class UserSignup(GenericAPIView):
    serializer_class = UserSerializer
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class UserLogin(GenericAPIView):
    serializer_class = LoginSerializer
    def post(self, request):
        data = request.data
        nm = data.get('username', '')
        pw = data.get('password', '')

        user = auth.authenticate(username=nm, password=pw)

        if user:
            auth_token = jwt.encode({'username': user.username}, 'password', algorithm='HS256')
            serializer = UserSerializer(user)

            data = {'user': serializer.data, 'token': auth_token}
            return Response(data, status=status.HTTP_202_ACCEPTED)
        
        return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)



