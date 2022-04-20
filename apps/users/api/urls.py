from django.urls import path
from apps.users.api.api import UserAPIView


urlpatterns = [
    path('user/', UserAPIView.as_view(), name='api_user'),
]