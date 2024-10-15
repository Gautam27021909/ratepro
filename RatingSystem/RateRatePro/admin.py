from django.contrib import admin
from .models import Users


class register(admin.ModelAdmin):
    list_display= ("username", "email","password")   
    
admin.site.register(Users, register)