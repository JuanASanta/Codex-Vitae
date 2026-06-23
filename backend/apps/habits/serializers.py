from .models import Habit
from rest_framework import serializers

class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = ["user", "name", "repeat_days", "active", "xp"]