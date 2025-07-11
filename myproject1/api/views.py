from django.shortcuts import render
from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from django.http import HttpResponse , JsonResponse

from .serializers import StudentSerializer
import io
from rest_framework.parsers import JSONParser
def student_api(request):

    if request.method == "POST":
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

    elif request.method == "GET":

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
    elif request.method == "PUT":
        stream = io.BytesIO(request.body)
        data = JSONParser().parse(stream)
        
        
        id = data.get("id")  
        if not id:
            return JsonResponse({"error": "ID is required for update"}, status=400)
        stu = Student.objects.get(id = id)
        serializer = StudentSerializer(stu,partial = True,data=data)
        if serializer.is_valid():
                serializer.save()
                return JsonResponse({"msg": "data created"}, status=201)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == "DELETE":
        stream = io.BytesIO(request.body)
        data = JSONParser().parse(stream)
        
        
        id = data.get("id")  
        if not id:
            return JsonResponse({"error": "ID is required for update"}, status=400)
        stu = Student.objects.get(id = id)
        stu.delete()
        return JsonResponse({"msg": "data deleted"}, status=201)
