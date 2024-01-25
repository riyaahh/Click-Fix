from django.urls import path,include
from .import views
from . views import index,about,contact,service,login


urlpatterns = [
    path('',index,name="dashboard"),
    path('about/', views.about ,name="about"),
    path('contact/', views.contact ,name="contact"),
    path('service/', views.service,name="service"),
    path('login/', views.login ,name="login"),
    # path('register' , views.register, name='register'),
    # path('user',views.user,name="user")
]

