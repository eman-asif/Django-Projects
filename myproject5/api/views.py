from rest_framework.generics import GenericAPIView
from rest_framework.mixins import (
    ListModelMixin, CreateModelMixin,
    RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
)
from .models import Student
from .serializers import StudentSerializer

class StudentAPI(GenericAPIView,
                 ListModelMixin,
                 CreateModelMixin,
                 RetrieveModelMixin,
                 UpdateModelMixin,
                 DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, pk=None):
        if pk:
            return self.retrieve(request, pk=pk)
        return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, pk):
        return self.update(request, pk=pk)

    def patch(self, request, pk):
        return self.partial_update(request, pk=pk)

    def delete(self, request, pk):
        return self.destroy(request, pk=pk)
