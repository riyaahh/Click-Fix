from django.urls import path,include
from .import views
from .views import book,books


urlpatterns = [
      path('bookings',book,name="book"),
      path('bookform',books,name="bookform")
]