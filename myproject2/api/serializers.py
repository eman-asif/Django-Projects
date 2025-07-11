from rest_framework import serializers
from .models import Student
"""Model serializer"""
class StudentSerializer(serializers.ModelSerializer):
    def start_with_e(value):
        if value[0].lower() != "e":
            raise serializers.ValidationError("Name should start with E")
        return value
    name = serializers.CharField(validators = [start_with_e])
    class Meta:
        model = Student
        fields = "__all__" # exclude = ["age"]
        # read_only_fields = ["name","age"]