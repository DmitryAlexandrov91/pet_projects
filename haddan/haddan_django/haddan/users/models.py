"""Модели приложения users."""
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Модель пользователя."""
