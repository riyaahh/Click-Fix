from django.urls import path,include
from .import views
from .views import index,about,contact,service,book


urlpatterns = [
    path('',index,name="dashboard"),
    path('index',index,name="index"),
    path('about',about,name="about"),
    path('contact',contact,name="contact"),
    path('service',service,name="service"),
    path('bookings',book,name="book")
]