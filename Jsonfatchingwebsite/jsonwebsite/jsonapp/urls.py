from . import views
from django.urls import path

urlpatterns = [
    path('',views.home,name='home'),
    path('info/<int:id>',views.meal_detail,name='meal_detail'),
]