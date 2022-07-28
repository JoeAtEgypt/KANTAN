from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

from rest_framework import serializers

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['phone'] = user.phone or None
        token['name'] = user.name
        token["id"] = user.id
        token["email"] = user.email

        return token


class UserSerializer(serializers.Serializer):
    phone = serializers.CharField()
    name = serializers.CharField()
    password = serializers.CharField(write_only=True, min_length=5)
    email = serializers.EmailField(allow_null=True, required=False)

    def validate(self, attrs):
        if attrs.get('email'):
            attrs['email'] = attrs.get('email').lower()
        if get_user_model().objects.filter(phone=attrs.get('phone'), is_active=True).first() is not None:
            raise ValidationError('User with this phone already exists')
        else:
            return attrs

    def create(self, validated_data):
        """ Create a User with encrypted password and return it """
        return get_user_model().objects.create_user(**validated_data)
