from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken

from apps.users.api.serializers import UserTokenSerializer

from datetime import datetime
from django.contrib.sessions.models import Session

# Create your views here.
class UserToken(APIView):
    def get(self, request, *args, **kwargs):
        username = request.GET.get('username')
        try: 
            user_token= Token.objects.get(
                user=UserTokenSerializer().Meta.model.objects.filter(username=username).first())
            return Response({'token':user_token.key})    
        except Exception:
            return Response({"error":'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)       

class Login(ObtainAuthToken):
    
    def post(self, request, *args, **kwargs):
        login_serializer = self.serializer_class(data=request.data, context = {'request': request})
        if login_serializer.is_valid():
            user=login_serializer.validated_data['user']
            if user.is_active:
                token, created =Token.objects.get_or_create(user=user)
                user_serializer = UserTokenSerializer(user)
                if created:
                    return Response({
                        'token': token.key,
                        'user': user_serializer.data,
                        'message': 'Login successfully!'
                    }, status=status.HTTP_201_CREATED)
                else: 
                    #This will disconnect the user from any active session if try to log in while another session in is active, finish on line 34
                    all_sessions = Session.objects.filter(expire_date__gte = datetime.now())
                    if all_sessions.exists():
                        for session in all_sessions:
                            session_data = session.get_decoded()
                            if user.id == int(session_data.get('_auth_user_id')):
                                session.delete()

                    token.delete()   

                    token =Token.objects.create(user=user) 
                    return Response({
                        'token': token.key,
                        'user': user_serializer.data,
                        'message': 'Login Session has been successfully!'
                    }, status=status.HTTP_201_CREATED)
                    '''use next line only if desired to kick the user out of the session without login

                    return Response({'error': 'user is already logged in, loging you out'}, status=status.HTTP_201_CREATED)

                    '''
            else:
                return Response('User is not active, please try again Later', status = status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({'error': 'User or password is incorrect'}, status = status.HTTP_400_BAD_REQUEST)

        return Response({'message','You have been successfully validated!'}, status=status.HTTP_200_OK)    

class Logout(APIView):
    
    def get(self, request, *args, **kwargs):
        try:
            token = request.GET.get('token')
            token = Token.objects.filter(key=token).first()
            
            if token:
                user = token.user
                all_sessions = Session.objects.filter(expire_date__gte = datetime.now())
                if all_sessions.exists():
                    for session in all_sessions:
                        session_data = session.get_decoded()
                        if user.id == int(session_data.get('_auth_user_id')):
                            session.delete()
                token.delete()    

                session_message = "Session Deleted"            
                token_message = "Token Deleted"
                return Response({'token_message':token_message, 'session_message': session_message}, status=status.HTTP_200_OK)  
            return Response({'error': 'User or has not been found'}, status = status.HTTP_400_BAD_REQUEST)  
        except:
            return Response({'error': 'Token has not been found in request'}, status = status.HTTP_409_CONFLICT)  
