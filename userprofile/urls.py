from django.urls import path
from userprofile import views

urlpatterns = [
    path("your-profile", views.userprofile, name="userprofile"),
    
]