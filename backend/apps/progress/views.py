from django.shortcuts import render, get_object_or_404
from .serializers import HabitCompletionSerializer
from .models import HabitCompletion
from rest_framework import permissions, viewsets
from rest_framework.exceptions import PermissionDenied

# Create your views here.
class HabitCompletionViewSet(viewsets.ModelViewSet):
    """
    Endpoint que permite listar y detallar los registros de hábitos completados.
    """

    serializer_class = HabitCompletionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return HabitCompletion.objects.filter(habit__user=self.request.user)
    
    def perform_create(self, serializer):
        habit = serializer.validated_data["habit"]

        if habit.user != self.request.user:
            raise PermissionDenied("No puedes completar este hábito.")

        serializer.save()