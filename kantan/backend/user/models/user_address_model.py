from django.db import models
from django.core.exceptions import ValidationError

from .user_model import User
from ..helpers.user_address_cities import CITIES_OPTIONS


def validate_phone(phone):
    if not phone.startswith('01'):
        raise ValidationError('Th phone number is not valid')


class UserAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="User")
    name = models.CharField(max_length=60)
    phone = models.CharField(max_length=11, help_text="Max Length equals 11 numbers", validators=[validate_phone])
    email = models.EmailField(blank=True, null=True)
    city = models.CharField(max_length=255, choices=CITIES_OPTIONS)
    address = models.CharField(max_length=255)
    building = models.CharField(max_length=60)
    floor = models.CharField(max_length=60)
    apartment = models.CharField(max_length=60)
    is_default = models.BooleanField(default=False)

    def __str__(self):
        return self.name

