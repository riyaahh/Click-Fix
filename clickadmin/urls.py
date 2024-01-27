from django.urls import path,include

from clickadmin import views
from clickadmin.views import index,about,contact,service

from .import views



urlpatterns = [
    path('',views.index,name="home"),
    path('about/', views.about ,name="about"),
    path('contact/', views.contact ,name="contact"),
    path('service/', views.service,name="service"),
    path('login/', views.signin ,name="login"),

    path('admin-dashboard',views.admin_dashboard,name='customer_dashboard')
]

