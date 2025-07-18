from django.contrib import admin
from .models import NewStudent
# Register your models here.
@admin.register(NewStudent)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["id",'name',"age","email", "passby"]