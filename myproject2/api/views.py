from django.shortcuts import render
from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from django.http import HttpResponse , JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from django.views import View

from .serializers import StudentSerializer
import io
from rest_framework.parsers import JSONParser
def student_detail(request,pk):
    stu = Student.objects.get(id=pk)
    ser = StudentSerializer(stu)
    return JsonResponse(ser.data,safe = False)

def student_list(request):
    stu = Student.objects.all()
    ser = StudentSerializer(stu,many = True)
    return JsonResponse(ser.data,safe = False)
from django.views import View
@method_decorator(csrf_exempt, name = "dispatch")
# @csrf_exempt
class StudentAPI(View):
    def get(self, request,*args , **kwargs):
        id = request.GET.get("id") 
        if id:
            try:
                stu = Student.objects.get(id=id)
                serializer = StudentSerializer(stu)
                return JsonResponse(serializer.data, safe=False)
            except Student.DoesNotExist:
                return JsonResponse({"error": "Student not found"}, status=404)
        else:
            stu = Student.objects.all()
            serializer = StudentSerializer(stu, many=True)
            return JsonResponse(serializer.data, safe=False)
    def post(self, request,*args , **kwargs):
        try:
            stream = io.BytesIO(request.body)
            data = JSONParser().parse(stream)
            serializer = StudentSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({"msg": "data created"}, status=201)
            return JsonResponse(serializer.errors, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    def put(self, request,*args , **kwargs):
        stream = io.BytesIO(request.body)
        data = JSONParser().parse(stream)
        
        
        id = data.get("id")  
        if not id:
            return JsonResponse({"error": "ID is required for update"}, status=400)
        stu = Student.objects.get(id = id)
        serializer = StudentSerializer(stu,partial = True,data=data)
        if serializer.is_valid():
                serializer.save()
                return JsonResponse({"msg": "Updated"}, status=201)
        return JsonResponse(serializer.errors, status=400)
    def delete(self, request,*args , **kwargs):
        stream = io.BytesIO(request.body)
        data = JSONParser().parse(stream)
        
        
        id = data.get("id")  
        if not id:
            return JsonResponse({"error": "ID is required for update"}, status=400)
        stu = Student.objects.get(id = id)
        stu.delete()
        return JsonResponse({"msg": "data deleted"}, status=201)
