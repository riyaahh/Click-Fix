from django.urls import path
from .import views
 





urlpatterns = [

    path('cdadmin',views.registration,name="home"),
    # path('admin','admin/registration.html',index,name="home"),
    
    ]