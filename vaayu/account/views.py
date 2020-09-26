from django.shortcuts import render
from .forms import CreateUser,NgoUser
from .models import *
# Create your views here.
def index(request):
    return render(request,"index.html")

def RegisterAsUser(request):
    form = CreateUser()
    if request.method == 'POST':
        form = CreateUser(request.post)
        if form.is_valid():
            user_form = user(
                fname = form.cleaned_data['fname'],
                lname = form.cleaned_data['lname'],
                email = form.cleaned_data['email'],
                phone = form.cleaned_data['phone'],
                password1 = form.cleaned_data['password1'],
                password2 = form.cleaned_data['password2'],
                Address = form.cleaned_data['address'],
                country = form.cleaned_data['country'],
                pincode = form.cleaned_data['pincode'],
            )




    return render(request,"register-donor.html")

def RegisterAsNgo(request):
    return render(request,"register-ngo.html")

def LoginAsUser(request):
    return render(request,"login.html")


def LoginAsNgo(request):
    return render(request,"login-ngo.html")
