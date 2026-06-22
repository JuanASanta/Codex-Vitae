from django.urls import path
from .views import MeViewSet


urlpatterns = [
    path("me/", MeViewSet.as_view(), name="me"),
]

