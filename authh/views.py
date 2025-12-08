from django.shortcuts import render

# Create your views here.
def loginpage(request):
    return render(request, "login.html")

def signuppage(request):
    return render(request, "signup.html")