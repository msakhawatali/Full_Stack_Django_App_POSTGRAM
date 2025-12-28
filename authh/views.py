from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def loginpage(request):
    return render(request, "login.html")

def signuppage(request):
    return render(request, "signup.html")

def signupurl(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        fir_name = request.POST.get("f_name")
        las_name = request.POST.get("l_name")
        passw = request.POST.get("password")

        User.objects.create_user(username = username, email = email, first_name = fir_name, last_name = las_name, password = passw)

        messages.success(request, "Signup Done, Please Login to Continue...")

    return redirect("/auth/login")


def loginurl (request):
    if request.method == 'POST':
        usern = request.POST.get("username")
        passw = request.POST.get("password")

        check = authenticate(username = usern, password = passw)

        if check:
            login(request, check)
            messages.success(request, "Login Successfully done..")
            
        else:
            messages.warning(request, "Please enter viald Credentials...")
        return redirect("/auth/login")
    
def logouturl(request):
    logout(request)
    return redirect("/auth/login")