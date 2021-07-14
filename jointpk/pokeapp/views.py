from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, "dashboard.html")

def login(request):
    return render(request, "login.html")

def reg(request):
    return render(request, "reg.html")

def profile(request):
    return render(request, "profile.html")