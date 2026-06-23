from django.urls import path, include
from .views import HabitCompletionViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r"", HabitCompletionViewSet, basename="habitscompletion")

urlpatterns = [
    path("", include(router.urls)),
]
