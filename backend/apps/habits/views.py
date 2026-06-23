from django.shortcuts import render
from rest_framework import permissions, viewsets
from .serializers import HabitSerializer
from .models import Habit


# Create your views here.
class HabitViewSet(viewsets.ModelViewSet):
    """
    Endpoint para ver y crear habitos
    """

    serializer_class = HabitSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)