from django.contrib import admin

from .models import Meals

# Register your models here.

class MealAdmin(admin.ModelAdmin):
    list_display=['name','category','area','instructions','slug']
admin.site.register(Meals,MealAdmin)