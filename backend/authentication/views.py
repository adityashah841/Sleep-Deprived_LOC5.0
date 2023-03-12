from django.contrib.auth import authenticate, login
from rest_framework import serializers, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import CustomUser

class LoginSerializer(serializers.Serializer):
    # email = serializers.EmailField()
    # password = serializers.CharField()
    class Meta:
        model = CustomUser
        fields = ["email", "password"]

    # def validate(self, attrs):
    #     email = attrs.get('email')
    #     password = attrs.get('password')

    #     # if email and password:
    #     if email:
    #         user = authenticate(email=email, password=password)
    #         if user:
    #             if user.is_active:
    #                 attrs['user'] = user
    #             else:
    #                 msg = 'User account is disabled.'
    #                 raise serializers.ValidationError(msg)
    #         else:
    #             msg = 'Unable to log in with provided credentials.'
    #             raise serializers.ValidationError(msg)
    #     else:
    #         msg = 'Must include "email" and "password".'
    #         raise serializers.ValidationError(msg)

    #     return attrs

class SignupSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True, 'style': {'input_type': 'password'}}
        }

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError("Passwords do not match.")
        return data

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        serializer = LoginSerializer(data=request.data)
        print(request.data)
        user = authenticate(email=request.data['email'], password=request.data['password'])
        print(user)
        if user:
            login(request, user)
            return Response({'detail': 'Logged in successfully.'})
        # if serializer.is_valid():
        #     # user = serializer.validated_data['user']
        #     # login(request, user)
        #     return Response({'detail': 'Logged in successfully.'})
        else:
            return Response("Invalid Credentials", status=status.HTTP_400_BAD_REQUEST)

class SignupView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'detail': 'Account created successfully.'})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
