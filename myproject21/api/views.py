from rest_framework.viewsets import ModelViewSet
from .models import NewStudent
from .serializers import NewStudentSerializer
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated , IsAuthenticatedOrReadOnly
from rest_framework.throttling import AnonRateThrottle , UserRateThrottle 
from rest_framework.generics import ListAPIView
# from .throttling import EmanRateThrottle
# from rest_framework_simplejwt.authentication import JWTAuthentication
# from .custompermissions import MyPermission


class StudentList(ListAPIView):
    queryset = NewStudent.objects.all()
    serializer_class = NewStudentSerializer

    def get_queryset(self):
        user = self.request.user
        # return super().get_queryset()
        return NewStudent.objects.filter(passby = 'user1')

# class StudentViewSet(ModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     authentication_classes = [SessionAuthentication]
#     permission_classes = [IsAuthenticatedOrReadOnly]
    # throttle_classes = [AnonRateThrottle, EmanRateThrottle]
    
    