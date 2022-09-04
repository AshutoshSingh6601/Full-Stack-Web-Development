from django.contrib import admin

from . models import Author, Book, Publisher

# Register your models here.

class PublisherAdmin(admin.ModelAdmin):
    list_display=['name', 'address', 'city', 'state', 'country', 'website'] 

admin.site.register(Publisher,PublisherAdmin)

class AuthorAdmin(admin.ModelAdmin):
    list_display=['salutation', 'first_name', 'last_name', 'email'] 
admin.site.register(Author,AuthorAdmin)

class BookAdmin(admin.ModelAdmin):
    list_display=['title','authors','publishers','publication_date']
admin.site.register(Book,BookAdmin)