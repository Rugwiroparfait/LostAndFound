from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import UserSerializer, UserRegistrationSerializer


class RegisterView(generics.CreateAPIView):
    permission_classes =  (AllowAny,)
    serializer_class = UserRegistrationSerializer

class UserProfileView(generics.RetrieveUpdateAPIView):
    """
    UserProfileView is a view that allows authenticated users to retrieve and update their profile information.

    Attributes:
        permission_classes (tuple): A tuple containing the permission classes that are required to access this view.
        serializer_class (class): The serializer class that should be used for validating and deserializing input, and for serializing output.

    Methods:
        get_object(self):
            Returns the user object associated with the current request.
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user
    
