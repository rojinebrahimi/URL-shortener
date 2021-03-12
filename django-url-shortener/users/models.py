from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    email = models.EmailField(max_length=128, null=False, blank=True, unique=True)

    def __str__(self):
        return self.email

    def lowercase_email(self):
        return self.email.lower()

