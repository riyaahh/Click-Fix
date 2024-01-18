from django.urls import path,include
from .import views
from .views import index,about,contact,service,login


urlpatterns = [

    path('',index,name="dashboard"),
    path('index',index,name="index"),
    path('about',about,name="about"),
    path('contact',contact,name="contact"),
    path('service',service,name="service"),
<<<<<<< HEAD
    path('login',login,name="login")

]
=======
    path('login',login,name="login"),
]
    
   
>>>>>>> 3f26a95bf680c7180a03b4fc30c19c19c369e106
