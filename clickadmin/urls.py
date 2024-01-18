from django.urls import path,include
from .import views
from .views import index,about,contact,service,login


urlpatterns = [
    path('login',login,name="login"),
    path('',index,name="dashboard"),
    path('index',index,name="index"),
    path('about',about,name="about"),
    path('contact',contact,name="contact"),
    path('service',service,name="service"),
<<<<<<< HEAD
   
=======
<<<<<<< HEAD
    path('login',login,name="login")

]
=======
    path('login',login,name="login"),
>>>>>>> 5957d7d3a8c0223b75313418843fd803ce754d0e
]
    
   
>>>>>>> 3f26a95bf680c7180a03b4fc30c19c19c369e106
