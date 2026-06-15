from django.db import models
from ..habits.models import Habit

class HabitCompletion(models.Model):
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["habit", "date"], name="unique_habit_per_day")
        ]