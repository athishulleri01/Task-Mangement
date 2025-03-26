from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "status", "created_at", "completed_at")  
    search_fields = ("name", "status") 
    list_filter = ("status", "created_at")  
    ordering = ("-created_at",)  
    filter_horizontal = ("assigned_users",) 

