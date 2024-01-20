from django.urls import path,include
from .import views
from .views import index,about,contact,service,login


urlpatterns = [
    path('',index,name="dashboard")
]

