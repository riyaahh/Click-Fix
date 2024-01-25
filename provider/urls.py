from django.urls import path,include
from .import views



urlpatterns = [
      path('bookings',views.bookings,name="bookings"),
      path('bookform',views.bookform,name="bookform"),
]