from django.contrib import admin
from .models import NewStudent 
@admin.register(NewStudent)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["id",'name',"age","email", "passby"]
