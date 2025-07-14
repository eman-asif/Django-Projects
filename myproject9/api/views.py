from rest_framework.viewsets import ReadOnlyModelViewSet
from .models import Student
from .serializers import StudentSerializer

class StudentReadOnlyViewSet(ReadOnlyModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
