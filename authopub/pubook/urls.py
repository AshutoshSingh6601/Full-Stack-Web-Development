from . import views
from django.urls import path

urlpatterns = [
    path('',views.publisher_form,name='publisher_form'),
    path('author/',views.author_form,name='author_form'),
    path('book/',views.book_form,name='book_form'),
    path('book_detail/',views.book_detail,name='book_detail'),
    path('author_detail/<int:id>',views.author_detail,name='author_detail'),
    path('publisher_detail/<int:id>',views.publisher_detail,name='publisher_detail'),
    # path('more_then_two/<int:id>', views.more_then_two, name='more_then_two'),
]