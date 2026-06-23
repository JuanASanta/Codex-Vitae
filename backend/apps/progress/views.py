from django.shortcuts import render
from .serializers import HabitCompletionSerializer
from .models import HabitCompletion
from rest_framework import permissions, viewsets

# Create your views here.
class HabitCompletionViewSet(viewsets.ModelViewSet):
    """
    Endpoint que permite listar y detallar los registros de hábitos completados.
    """

    serializer_class = HabitCompletionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return HabitCompletion.objects.filter(habit__user=self.request.user)
    