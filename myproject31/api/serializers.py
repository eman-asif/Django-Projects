from rest_framework import serializers
from .models import NewStudent
"""Model serializer"""
class NewStudentSerializer(serializers.ModelSerializer):
    def start_with_e(value):
        if value[0].lower() != "e":
            raise serializers.ValidationError("Name should start with E")
        return value
    name = serializers.CharField(validators = [start_with_e])
    class Meta:
        model = NewStudent
        fields = "__all__" # exclude = ["age"]
                         # read_only_fields = ["name","age"]      
'''Serializer:'''
# class StudentSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=100)
#     age = serializers.IntegerField()
#     email = serializers.EmailField()

#     def create(self, validated_data):
#         return Student.objects.create(**validated_data)
    
#     def update(self , instance , validated_data):
#         instance.name = validated_data.get("name", instance.name)
#         instance.age = validated_data.get("age", instance.age)
#         instance.email = validated_data.get("email", instance.email)
#         instance.save()
#         return instance
    
#     def validate_age(self,value):
#         if value>= 30:
#             raise serializers.ValidationError("Too Old")
#         return value
    
#     def validate(self, data):
#         name = data.get("name")
#         age = data.get("age")
#         # if name and age:
#         if name.lower() == "eman" and age > 25:
#             raise serializers.ValidationError("Not allowed")
#         return data
