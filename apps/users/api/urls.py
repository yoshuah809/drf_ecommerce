from django.urls import path
from apps.users.api.api import UserAPIView, user_detail_view


urlpatterns = [
    path('users/', UserAPIView, name='api_user'),
    path('users/<int:pk>/', user_detail_view, name='user_detail_view'),


    
]