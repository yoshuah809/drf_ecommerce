from datetime import timedelta
from django.conf import settings
from django.utils import timezone
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed

    

class ExpiringTokenAuthentication(TokenAuthentication):
    
    def expires_in(self, token):
        time_elapsed = timezone.now() - token.created
        remaining_time = timedelta(seconds=settings.TOKEN_EXPIRE_AFTER_SECONDS) - time_elapsed
        return remaining_time


    def is_token_expired(self, token):
        return self.expires_in(token) < timedelta(secons = 0)
    
    def token_expire_handler(self,token):
        is_expired = self.is_token_expired(token)
        if is_expired:
          print('EXPIRED TOKEN')

        return is_expired  

    def authenticate_credentials(self, key):
        try:
            token = self.get_model().objects.get(key = key)
        except self.model.DoesNotExist:
            raise AuthenticationFailed('Token is Invalid')

        if not token.user.is_active:
            raise AuthenticationFailed('User is not active or does not exist')

        is_expired = self.token_expire_handler(token.user)    
        if is_expired:
            raise AuthenticationFailed('Your Token has expired')