from rest_framework.authentication import BaseAuthentication
from django.contrib.auth.models import User
from rest_framework.exceptions import AuthenticationFailed

class CustomAuthentciation(BaseAuthentication):

    def authenticate(Self,request):
        username = request.GET.get("username")
        if username is None:
            return None
        
        try:
            user  = User.objects.get(username= username)

        except User.DoesNotExist: 
            raise AuthenticationFailed("No such user")