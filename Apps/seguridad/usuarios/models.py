from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    rol = models.CharField(max_length=50, choices=[('admin', 'Admin'), ('user', 'User')])

