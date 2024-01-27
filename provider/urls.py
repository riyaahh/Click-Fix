from django.urls import path,include
from .import views



urlpatterns = [
    path('',views.provider_dashboard,name='provider_dashboard'),
      path('bookings',views.bookings,name="bookings"),
      path('bookform',views.bookform,name="bookform"),
      path('prof',views.prof,name="prof"),
      path('profform',views.profform,name="profform")
]