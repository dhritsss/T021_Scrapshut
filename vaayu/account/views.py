from django.shortcuts import render
from .forms import CreateUser,NgoUser
from .models import *
# Create your views here.
def index(request):
    return render(request,"index.html")

def RegisterAsUser(request):




    return render(request,"register-donor.html")

def RegisterAsNgo(request):
    return render(request,"register-ngo.html")

def LoginAsUser(request):
    return render(request,"login.html")


def LoginAsNgo(request):
    return render(request,"login-ngo.html")
