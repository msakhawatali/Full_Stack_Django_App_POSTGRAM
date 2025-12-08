from django.urls import path
from authh import views

urlpatterns = [
    path("login", views.loginpage, name = "login"),
    path("signup", views.signuppage, name = "signup"),
]