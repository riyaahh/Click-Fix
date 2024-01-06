from django.urls import path,include
from .import views
from provider.views import servicesmain


urlpatterns = [
    
    path('', views.index),
    path('',servicesmain,name="service"),
]