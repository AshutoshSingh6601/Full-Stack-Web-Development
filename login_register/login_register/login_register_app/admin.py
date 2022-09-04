from atexit import register
from unittest import case
from django.contrib import admin


from .models import Login, Register 
# Register your models here.

class LoginAdmin(admin.ModelAdmin):
    list_display=['username', 'password']
admin.site.register(Login,LoginAdmin)

class RegisterAdmin(admin.ModelAdmin):
    list_display=['username', 'password', 'address']
admin.site.register(Register,RegisterAdmin)