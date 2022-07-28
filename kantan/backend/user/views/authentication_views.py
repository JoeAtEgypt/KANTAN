from django.shortcuts import get_object_or_404

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotAcceptable

from ..models.user_model import User
from ..models.otp_model import OTP
from ..serializers.user_serializer import UserSerializer
from ..helpers.user_helpers import calculate_time_diff

class MyTokenObtainPairView(TokenObtainPairView):
    permission_classes = []
    authentication_classes = []
    serializer_class = MyTokenObtainPairSerializer


class SignUpAPI(CreateAPIView, UpdateAPIView):
    serializer_class = UserSerializer

    def get_object(self):
        return User.objects.get(phone=self.request.data.get('phone'))

    def update(self, request, *args, **kwargs):
        """ Takes newly registered phone number and verifies it using OTP """
        user = self.get_object()
        otp = get_object_or_404(OTP, user=user)

        if not calculate_time_diff(otp.modified) < 180.0 or otp.code != self.request.data.get('code'):
            raise NotAcceptable("Code Expired or invalid")
        elif not user.is_active:
            user.is_active = True
            user.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_200_OK)


