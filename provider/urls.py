from django.urls import path,include
from .import views
from .views import index,about,contact,service


urlpatterns = [
    path('',index,name="home"),
    path('','provider/index.html',index,name="home"),

    path('',about,name="home1"),
    path('',contact,name="home2"),
    path('',service,name="home3"),
]