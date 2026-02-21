from django.contrib import admin
from .models import Student,Notification

# Register your models here.
class studentAdmin(admin.ModelAdmin):
    list_display=("name","roll_number")
    search_fields=("name","roll_number")
admin.site.register(Student,studentAdmin)
admin.site.register(Notification)