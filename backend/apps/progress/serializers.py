from .models import HabitCompletion
from rest_framework import serializers

class HabitCompletionSerializer(serializers.ModelSerializer):
    class Meta:
        model = HabitCompletion
        fields = ["habit", "date"]