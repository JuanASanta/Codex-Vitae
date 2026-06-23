from django.urls import path, include
from .views import HabitViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r"", HabitViewSet, basename="habits")

urlpatterns = [
    path("", include(router.urls)),
]

