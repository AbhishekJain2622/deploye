from .views import (
    ContactAPIView
 
)
from django.urls import path


urlpatterns = [
    path("contect/", ContactAPIView.as_view(), name="contact"),
 

]