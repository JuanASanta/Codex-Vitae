from .models import Habit
from rest_framework import serializers

class HabitSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Habit
        fields = ["user", "name", "repeat_days", "active", "xp"]