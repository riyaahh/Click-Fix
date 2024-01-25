
from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.signin,name='login'),
    path('register' , views.register, name='register'),
    path('user',views.userData,name="user"),
]