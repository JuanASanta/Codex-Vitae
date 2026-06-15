from django.db import models
from ..users.models import CustomUser


# Create your models here.
class Habit(models.Model):
    user = models.ForeignKey(CustomUser, verbose_name="User", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    repeat_days = models.JSONField()
    active = models.BooleanField(default=True)
    xp = models.IntegerField(default=10)

    def __str__(self):
        return self.name