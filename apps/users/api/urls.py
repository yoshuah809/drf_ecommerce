from django.urls import path
from apps.users.api.api import UserAPIView, user_detail_view


urlpatterns = [
    path('user/', UserAPIView, name='api_user'),
    path('user/<int:pk>/', user_detail_view, name='user_detail_view'),


    
]