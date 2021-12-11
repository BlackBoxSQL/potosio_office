from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('client', 'client'),
        ('photographer', 'photographer'),
    )
    user_type = models.CharField(max_length=50, choices=USER_TYPE_CHOICES)

    email = models.EmailField(
        blank=False, max_length=254, verbose_name="email address")

    USERNAME_FIELD = "username"   # e.g: "username", "email"
    EMAIL_FIELD = "email"         # e.g: "email", "primary_email"
