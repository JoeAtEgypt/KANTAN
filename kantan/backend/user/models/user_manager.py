from django.contrib.auth.models import BaseUserManager

from .user_model import User


class UserManager(BaseUserManager):

    def validate_phone(self, phone):
        """ Validates phone number """
        if not phone.startswith('01'):
            message = "Invalid phone number"
            return message, False
        if not phone:
            message = "You must enter phone number"
            return message, False
        return '', True

    def create_user(self, phone, password=None, **extra_fields):
        """Creates and saves a new user"""
        msg, valid = self.validate_phone(phone)
        try:
            user = User.objects.get(phone=phone, is_active=False)
            user.name = extra_fields['name']
            user.email = extra_fields['email']
        except:
            user = self.model(phone, **extra_fields)
            user.is_active = False

        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, phone, password):
        """Creates and saves superuser"""
        user = self.create_user(phone, password)
        user.is_active = True
        user.is_superuser = True
        user.is_staff = True

        return user


