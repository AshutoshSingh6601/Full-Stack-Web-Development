from django.contrib import admin

from .models import Loggin

# Register your models here.

class LogginAdmin(admin.ModelAdmin):
    list_display=['username','password','email','date_time']
admin.site.register(Loggin,LogginAdmin)