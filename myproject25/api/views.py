from rest_framework.viewsets import ModelViewSet
from .models import NewStudent
from .serializers import NewStudentSerializer
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated , IsAuthenticatedOrReadOnly
from rest_framework.throttling import AnonRateThrottle , UserRateThrottle 
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter , OrderingFilter
# from .throttling import EmanRateThrottle
# from rest_framework_simplejwt.authentication import JWTAuthentication
# from .custompermissions import MyPermission


class StudentList(ListAPIView):
    queryset = NewStudent.objects.all()
    serializer_class = NewStudentSerializer
    # filter_backends = [ OrderingFilter]
    # search_fields = ['^name']
    # ordering_fields = ['name','city']
    # filterset_fields = ['passby']