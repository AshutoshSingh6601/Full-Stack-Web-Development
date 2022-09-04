
from login_register_app import views
from django.urls import path

urlpatterns = [
    path('login/',views.login_form, name='login_form'),
    path('register',views.register_form, name='register_form'),
    path('store',views.store, name='store'),
]