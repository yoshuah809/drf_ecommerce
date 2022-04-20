from django.urls import path
from apps.users.api.api import UserAPIView


urlpatterns = [
    path('user/', UserAPIView, name='api_user'),
]