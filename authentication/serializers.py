from django.contrib.auth.models import User
from django.contrib.auth.models import UserManager

from rest_framework import serializers



class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255, min_length=8)
    first_name = serializers.CharField(max_length=255, min_length=2)
    last_name = serializers.CharField(max_length=255, min_length=2)
    password = serializers.CharField(max_length=255, min_length=8, write_only=True)


    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password')

    def validate(self, validated_data):
        if User.objects.filter(email=validated_data.get('email')).exists():
            raise serializers.ValidationError({'email': 'Email id already exists'})
        return super().validate(validated_data)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
        

class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=255, min_length=2)
    password = serializers.CharField(max_length=255, min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password')