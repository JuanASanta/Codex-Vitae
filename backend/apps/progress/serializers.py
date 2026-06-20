from .models import HabitCompletion
from rest_framework import serializers

class HabitCompletionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HabitCompletion
        fields = ["habit", "date"]