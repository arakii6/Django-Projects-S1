from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    phone_number = models.CharField(max_length = 100, unique = True, null = True)
    email = models.EmailField(unique = True, default = 'example@example.com')
    bio = models.CharField(max_length = 80)
    profile_image = models.ImageField(upload_to = 'profile')
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()
