from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from apps.users.models import User
from apps.users.api.serializers import UserSerializer
from rest_framework import status

@api_view(['GET', 'POST'])
def UserAPIView(request):

    # List
   if request.method == 'GET':
        users = User.objects.all() 
        users_serializer = UserSerializer(users, many=True)
        return Response(users_serializer.data, status=status.HTTP_200_OK)

    #Create
   if request.method == 'POST':
      user_serializer = UserSerializer(data=request.data )  
      if user_serializer.is_valid():
         user_serializer.save()
         return Response({'message': 'user created Successfully'}, status=status.HTTP_201_CREATED)
      return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)   

@api_view(['GET','PUT','DELETE'])
def user_detail_view(request, pk=None):
   #queryset
   user = User.objects.filter(id = pk).first()
   #Validation
   if user:

      #Retrieve user
      if request.method == 'GET':
         user_serializer = UserSerializer(user)
         return Response(user_serializer.data)

      #update user
      elif request.method == 'PUT':
        user_serializer = UserSerializer(user, data = request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)  

       #delete user
      elif request.method == 'DELETE':
         user.delete()
         return Response({'message': 'User has been deleted successfully!'})     

   return Response({'message': 'User has been deleted successfully'}, status=status.HTTP_400_BAD_REQUEST)  