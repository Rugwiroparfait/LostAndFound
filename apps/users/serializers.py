from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from typing import Any, Dict

# Dynamically retrieve the user model to support custom user models
User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the User model, providing serialization for user details.

    Attributes:
        Meta: Contains metadata for the serializer, including the model and fields to serialize.
    """
    class Meta:
        model = User  # The model to serialize
        fields = ('id', 'username', 'email', 'phone_number', 'address')
        read_only_fields = ('id',)

class UserRegistrationSerializer(serializers.ModelSerializer):
    """
    Serializer for user registration, including password handling.

    Attributes:
        password (CharField): A write-only field for the user's password.

    Methods:
        create: Creates a new user instance with the provided validated data.
    """
    username = serializers.CharField(write_only=True)
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(write_only=True)
    phone_number = serializers.CharField(write_only=True)
    address = serializers.CharField(write_only=True)

    class Meta:
        model = User  # The model to serialize
        fields = ('username', 'email', 'password', 'phone_number', 'address')

    def create(self, validated_data: Dict[str, Any]) -> Any:
        """
        Creates a new user instance with the provided validated data.

        Args:
            validated_data (Dict[str, Any]): The validated data for creating the user.

        Returns:
            User: The created user instance.
        """
        return User.objects.create_user(**validated_data)
