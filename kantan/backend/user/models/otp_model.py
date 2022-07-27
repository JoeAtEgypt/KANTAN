from django.db import models
from django_extensions.db.models import TimeStampedModel
from django.conf import settings


class OTP(TimeStampedModel):
    code = models.CharField(max_length=6)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        self.code

    def save(self, *args, **kwargs):
        import random
        self.code = create_activation_code(random.randint(1000, 9999))

    class Meta:
        verbose_name_plural = 'OTPs'
