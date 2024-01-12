from django.urls import path,include
from .import views
from .views import index,about,contact,service,login


urlpatterns = [
<<<<<<< HEAD
    path('',index,name="dashboard"),
    path('index',index,name="index"),
    path('about',about,name="about"),
    path('contact',contact,name="contact"),
    path('service',service,name="service"),
    path('login',login,name="login")
=======
    
    path('',views.index,name="index"),
    path('about',views.about,name="about"),
    path('contact',views.contact,name="contact"),
    path('service',views.service,name="service"),
>>>>>>> 0b728caec7e4944172b3924072923e6a48826768
    
]