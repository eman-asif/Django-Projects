from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status

class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={"request": request})
        
        if serializer.is_valid():  # Validate input
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'token': token.key,
                'user_id': user.pk,
                'email': user.email
            })
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# from rest_framework.authtoken.views import ObtainAuthToken
# from rest_framework.authtoken.models import Token
# from rest_framework.response import Response

# class CustomAuthToken(ObtainAuthToken):

#     def post(self, request, *args, **kwargs):
#         serializer = self.serializer_class(data= request.data, context= {"request": request})
#         user = self.validated_data["user"]
#         token , created = Token.objects.get_or_create(user= user)
#         return Response({
#             "token": token.key,
#             "user_id": user.pk,
#             "email": user.email
#             })