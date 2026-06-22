from django.shortcuts import render
from rest_framework import permissions, generics
from .models import CustomUser
from .serializers import UserSerializer

# Create your views here.
class MeViewSet(generics.RetrieveUpdateAPIView):
    """
    Endpoint para ver tu propio usuario
    """
    
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user