
from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.decorators import api_view , authentication_classes , permission_classes
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication,BaseAuthentication
from rest_framework.permissions import IsAuthenticated
@api_view(["GET","POST"])
def hello_world(request):
    if request.method == "GET":
        return Response({"msg":"hello world"})
    
    if request.method == "POST":
        return Response({"msg":"hello world from post"})
@api_view(["GET","PATCH","POST","DELETE","PUT"])
# @authentication_classes([BaseAuthentication])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def student_api(request,pk = None):
    if request.method == "POST":
        try:
            
            serializer = StudentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"msg": "data created"})
            return Response(serializer.errors, status=400)
        except Exception as e:
            return Response({"error": str(e)}, status=500)
    if request.method == "GET":
        id = pk
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
          
            return Response(serializer.data)
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many = True)
        return Response(serializer.data)
    if request.method == "DELETE":
        id = pk
        # id = request.data.get("id")  
        if not id:
            return Response({"error": "ID is required for update"}, status=400)
        stu = Student.objects.get(id = id)
        stu.delete()
        return Response({"msg": "data deleted"}, status=201)
    if request.method == "PATCH":
        id = request.data.get("id")  
        if not id:
                return Response({"error": "ID is required for update"}, status=400)
        stu = Student.objects.get(id = id)
        serializer = StudentSerializer(stu,partial = True,data=request.data)
        if serializer.is_valid():
                serializer.save()
                return Response({"msg": "Updated partially"}, status=201)
        return Response(serializer.errors, status=400)

    if request.method == "PUT":
        id = request.data.get("id")  
        if not id:
                return Response({"error": "ID is required for update"}, status=400)
        stu = Student.objects.get(id = id)
        serializer = StudentSerializer(stu,data=request.data)
        if serializer.is_valid():
                serializer.save()
                return Response({"msg": "Updated completely"}, status=201)
        return Response(serializer.errors, status=400)
# # def student_api(request):
# # from django.shortcuts import render
# # from .models import Student
# # from .serializers import StudentSerializer
# # from django.http import HttpResponse , JsonResponse
# # # Create your views here.
# # from django.views.decorators.csrf import csrf_exempt
# # from django.utils.decorators import method_decorator

# # from django.views import View

# # from .serializers import StudentSerializer
# # import io
# # from rest_framework.parsers import JSONParser
# # def student_detail(request,pk):
# #     stu = Student.objects.get(id=pk)
# #     ser = StudentSerializer(stu)
# #     return JsonResponse(ser.data,safe = False)

# # def student_list(request):
# #     stu = Student.objects.all()
# #     ser = StudentSerializer(stu,many = True)
# #     return JsonResponse(ser.data,safe = False)
# # from django.views import View
# # @method_decorator(csrf_exempt, name = "dispatch")
# # # @csrf_exempt
# # class StudentAPI(View):
# #     def get(self, request,*args , **kwargs):
# #         id = request.GET.get("id") 
# #         if id:
# #             try:
# #                 stu = Student.objects.get(id=id)
# #                 serializer = StudentSerializer(stu)
# #                 return JsonResponse(serializer.data, safe=False)
# #             except Student.DoesNotExist:
# #                 return JsonResponse({"error": "Student not found"}, status=404)
# #         else:
# #             stu = Student.objects.all()
# #             serializer = StudentSerializer(stu, many=True)
# #             return JsonResponse(serializer.data, safe=False)
# #     def post(self, request,*args , **kwargs):
# #         try:
# #             stream = io.BytesIO(request.body)
# #             data = JSONParser().parse(stream)
# #             serializer = StudentSerializer(data=data)
# #             if serializer.is_valid():
# #                 serializer.save()
# #                 return JsonResponse({"msg": "data created"}, status=201)
# #             return JsonResponse(serializer.errors, status=400)
# #         except Exception as e:
# #             return JsonResponse({"error": str(e)}, status=500)
# #     def put(self, request,*args , **kwargs):
# #         stream = io.BytesIO(request.body)
# #         data = JSONParser().parse(stream)
        
        
# #         id = data.get("id")  
# #         if not id:
# #             return JsonResponse({"error": "ID is required for update"}, status=400)
# #         stu = Student.objects.get(id = id)
# #         serializer = StudentSerializer(stu,partial = True,data=data)
# #         if serializer.is_valid():
# #                 serializer.save()
# #                 return JsonResponse({"msg": "updated"}, status=201)
# #         return JsonResponse(serializer.errors, status=400)
# #     def delete(self, request,*args , **kwargs):
# #         stream = io.BytesIO(request.body)
# #         data = JSONParser().parse(stream)
        
        
# #         id = data.get("id")  
# #         if not id:
# #             return JsonResponse({"error": "ID is required for update"}, status=400)
# #         stu = Student.objects.get(id = id)
# #         stu.delete()
# #         return JsonResponse({"msg": "data deleted"}, status=201)
# # # def student_api(request):

# # #     if request.method == "POST":
# # #         try:
# # #             stream = io.BytesIO(request.body)
# # #             data = JSONParser().parse(stream)
# # #             serializer = StudentSerializer(data=data)
# # #             if serializer.is_valid():
# # #                 serializer.save()
# # #                 return JsonResponse({"msg": "data created"}, status=201)
# # #             return JsonResponse(serializer.errors, status=400)
# # #         except Exception as e:
# # #             return JsonResponse({"error": str(e)}, status=500)

# # #     elif request.method == "GET":

# # #         id = request.GET.get("id") 
# # #         if id:
# # #             try:
# # #                 stu = Student.objects.get(id=id)
# # #                 serializer = StudentSerializer(stu)
# # #                 return JsonResponse(serializer.data, safe=False)
# # #             except Student.DoesNotExist:
# # #                 return JsonResponse({"error": "Student not found"}, status=404)
# # #         else:
# # #             stu = Student.objects.all()
# # #             serializer = StudentSerializer(stu, many=True)
# # #             return JsonResponse(serializer.data, safe=False)
# # #     elif request.method == "PUT":
# # #         stream = io.BytesIO(request.body)
# # #         data = JSONParser().parse(stream)
        
        
# # #         id = data.get("id")  
# # #         if not id:
# # #             return JsonResponse({"error": "ID is required for update"}, status=400)
# # #         stu = Student.objects.get(id = id)
# # #         serializer = StudentSerializer(stu,partial = True,data=data)
# # #         if serializer.is_valid():
# # #                 serializer.save()
# # #                 return JsonResponse({"msg": "data created"}, status=201)
# # #         return JsonResponse(serializer.errors, status=400)
# # #     elif request.method == "DELETE":
# # #         stream = io.BytesIO(request.body)
# # #         data = JSONParser().parse(stream)
        
        
# # #         id = data.get("id")  
# # #         if not id:
# # #             return JsonResponse({"error": "ID is required for update"}, status=400)
# # #         stu = Student.objects.get(id = id)
# # #         stu.delete()
# # #         return JsonResponse({"msg": "data deleted"}, status=201)

# # # def student_api(request):
# # #     if request.method == "POST":
# # #         try:
# # #             stream = io.BytesIO(request.body)
# # #             data = JSONParser().parse(stream)
# # #             serializer = StudentSerializer(data=data)
# # #             if serializer.is_valid():
# # #                 serializer.save()
# # #                 return JsonResponse({"msg": "data created"})
# # #             return JsonResponse(serializer.errors, status=400)
# # #         except Exception as e:
# # #             return JsonResponse({"error": str(e)}, status=500)
# # #     if request.method == "GET":
# # #         stream = io.BytesIO(request.body)
# # #         data = JSONParser().parse(stream)
# # #         id = data.get("id",None)
# # #         if id is not None:
# # #             stu = Student.objects.get(id=id)
# # #             serializer = StudentSerializer(stu)
          
# # #             return JsonResponse(serializer.data,safe = False)
# # #         stu = Student.objects.all()
# # #         s = StudentSerializer(stu , many = True)
# # #         # stu = n Student.objects.get(id=id)
# # #         serializer = StudentSerializer(stu)
          
# # #         return JsonResponse(serializer.data,safe = False)
