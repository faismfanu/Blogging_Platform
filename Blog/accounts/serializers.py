from rest_framework import serializers
from django.contrib.auth.models import User

# Define the serializer fields, including custom validation for email
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=65, min_length=8, write_only=True)
    email = serializers.EmailField(max_length=200, min_length=4)
    first_name = serializers.CharField(max_length=200, min_length=2)
    last_name = serializers.CharField(max_length=200, min_length=2)

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password']

    def validate(self, attrs):
        # Custom validation to check if email is already in use
        email = attrs.get('email','')
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email':('Email is already in use.')})
        return super().validate(attrs)
    
    def create(self, validated_data):
        # Method to create a new user instance with validated data
        return User.objects.create_user(**validated_data)
    
class LoginSerializer(serializers.ModelSerializer):
    # Serializer for user login
    password = serializers.CharField(max_length=65,min_length=8, write_only=True)
    username = serializers.CharField(max_length=255, min_length=2)

    class Meta:
        model = User
        fields = ['username','password']