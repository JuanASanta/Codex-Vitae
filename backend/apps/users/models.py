from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    character_name = models.CharField(max_length=100, blank=True, null=True)
    level = models.IntegerField(default=1)
    total_experience = models.IntegerField(default=0)
    created_at = models.DateField(auto_now_add=True)
    username = None  # Elimina el campo username

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.character_name if self.character_name else self.email}"