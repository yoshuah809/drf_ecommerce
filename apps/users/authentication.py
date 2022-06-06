from datetime import timedelta
from django.conf import settings
from django.utils import timezone
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed


    

class ExpiringTokenAuthentication(TokenAuthentication):
    expired=False

    def expires_in(self, token):
        time_elapsed = timezone.now() - token.created
        remaining_time = timedelta(seconds=settings.TOKEN_EXPIRE_AFTER_SECONDS) - time_elapsed
        return remaining_time


    def is_token_expired(self, token):
        return self.expires_in(token) < timedelta(seconds = 0)
    
    def token_expire_handler(self,token):
        is_expired = self.is_token_expired(token)
        if is_expired:
          self.expired=True
          user=token.user  
          token.delete()
          token = self.get_model().objects.create(user=user)

        return is_expired, token  

    def authenticate_credentials(self, key):
        message, token,user = None,None,None
        try:
            token = self.get_model().objects.select_related('user').get(key=key)
            user = token.user
        except self.get_model().DoesNotExist:
            message = 'Token is invalid'
            self.expired=True
            
        if token is not None:
           if not token.user.is_active:
            message = 'User is not active'   

           is_expired = self.token_expire_handler(token)    
           if is_expired:
              message = 'Your Token has expired'

        return(user, token, message, self.expired)   