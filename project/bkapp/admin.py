from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(book)
from django.contrib import admin
from .models import student

@admin.register(student)
class studentAdmin(admin.ModelAdmin):
    list_display = ('name','rollno')
