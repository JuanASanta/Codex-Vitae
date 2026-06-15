from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


# Create your models here.
class CustomUserManager(BaseUserManager):

    def create_user(self, email, password=None, **kwargs):
        """
        Crea y guarda un usuario con el email y la contraseña.
        """

        if not email:
            raise ValueError('El usuario debe tener un email')
        
        if not password:
            raise ValueError('El usuario debe tener una contraseña')

        user = self.model(
            email=self.normalize_email(email),
            **kwargs
        )
        
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    
    def create_superuser(self, email, password=None):
        """
        Crea y guarda un superusuario con el email y la contraseña.
        """

        return self.create_user(email, password, is_staff=True, is_superuser=True)
        
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    character_name = models.CharField(max_length=100, blank=True, null=True)
    level = models.IntegerField(default=1)
    total_experience = models.IntegerField(default=0)
    created_at = models.DateField(auto_now_add=True)
    username = None  # Elimina el campo username

    objects = CustomUserManager()
    
    

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.character_name if self.character_name else self.email}"