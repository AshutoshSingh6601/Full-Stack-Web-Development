from django.contrib import admin
from site1.models import Product
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display=['product_name','price','stock','description']

admin.site.register(Product,ProductAdmin)