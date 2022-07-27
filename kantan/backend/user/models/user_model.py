from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .user_manager import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    phone = models.CharField(max_length=11, unique=True, help_text="Max-length equals 11", verbose_name="Phone Number")
    name = models.CharField(max_length=255)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    email = models.EmailField(verbose_name="Email")

    USERNAME_FIELD = 'phone'

    objects = UserManager()




