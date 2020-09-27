from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import auth,User
from .forms import *
from .models import *



# Create your views here.
def index(request):
    return render(request,"index.html")

def RegisterAsUser(request):
    if request.method == "POST":
        return redirect('LoginAsUser')
    else:
        return render(request,"register-donor.html")
'''   
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        donar_form = DonarForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and donar_form.is_valid():
            user_form.save()
            donar_form.save()
            messages.success(request, ('Your profile was successfully updated!'))
            return redirect('LoginAsUser')
        else:
            messages.error(request, ('Please correct the error below.'))
            return render('RegisterAsUser')
    else:
        user_form = UserForm(instance=request.user)
        donar_form = DonarForm(instance=request.user.profile)
    return render(request, 'register-donar.html', {'user_form': user_form,'donar_form': donar_form})
'''
"""    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']

        email = request.POST['email']
        phone = request.POST['phone']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        Address = request.POST['address']
        country = request.POST['country']
        pincode = request.POST['pincode']

        if password1 == password2:
            if user.objects.filter(email=email).exists():
                messages.info(request, "Enter another email-id !!")
                return redirect("RegisterAsUser")
            else:
                user_view = user.objects.c(fname=fname, lname=lname, email=email, phone=phone,
                                                     password=password1, Address=Address, country=country,
                                                     pincode=pincode)
                user_view.save()
                messages.info(request, "user created")
                return redirect('LoginAsUser')
        else:
            print("the password and confirm password didn't match !!")
            return redirect('RegisterAsUser')
    else:
        return render(request, "register-donor.html")
"""
def RegisterAsNgo(request):
    if request.method == 'POST':
        return redirect('LoginAsNgo')
    else:
        return render(request,"register-ngo.html")
        '''
        user_form = UserForm(request.POST, instance=request.user)
        ngo_form = NGOForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and ngo_form.is_valid():
            user_form.save()
            ngo_form.save()
            messages.success(request, ('Your profile was successfully updated!'))
            return redirect('LoginAsNgo')
        else:
            messages.error(request, ('Please correct the error below.'))
            return render('RegisterAsNgo')
    else:
        user_form = UserForm(instance=request.user)
        ngo_form = NGOForm(instance=request.user.profile)
    return render(request, 'register-ngo.html', {'user_form': user_form,'ngo_form': ngo_form})
"""
    if request.method == 'POST':
        ngo_name = request.POST['first_name']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        ngo_email = request.POST['email']
        ngo_phone = request.POST['phone']
        ngo_address = request.POST['address']
        ngo_country = request.POST['country']
        ngo_pincode = request.POST['pincode']
        weblink = request.POST['weblink']

        if password1 == password2:
            if ngo.objects.filter(ngo_email = ngo_email).exists():
                messages.info(request, "Enter another email-id !!")
                return redirect("RegisterAsNgo")
            else:
                ngo_view = ngo.objects.create_user(ngo_name=ngo_name,ngo_email=ngo_email,ngo_phone=ngo_phone,ngo_pass=password1, ngo_address= ngo_address, ngo_country=ngo_country,ngo_pincode=ngo_pincode,weblink = weblink)
                ngo_view.save()
                messages.info(request, "ngo account created")
                return redirect('LoginAsNgo')
        else:
            print("the password and confirm password didn't match !!")
            return redirect('RegisterAsNgo')

    # return redirect('/')
    else:
        return render(request, "register-ngo.html")
    '''

def LoginAsUser(request):
    if request.method == 'POST':
        return redirect('RegisterAsUserSuccess')
    else:
        return render(request, "login.html")
        '''
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('UserDonation')
        else:
            messages.info(request,"Invalid credentials")
            return redirect('LoginAsUser')
            '''


def LoginAsNgo(request):
    if request.method == "POST":
        return redirect('NgoHomepage')
    else:
        return render(request, "login-ngo.html")
        ''' 
        ngo_email = request.POST['ngo_email']
        ngo_pass = request.POST['ngo_pass']

        ngo = auth.authenticate(ngo_email=ngo_email, ngo_pass=ngo_pass)

        if ngo is not None:
            auth.login(request,ngo)
            return redirect('NgoRequirement')
        else:
            messages.info(request,"Invalid credentials")
            return redirect('LoginAsNgo')
            '''


def RegisterAsUserSuccess(request):
    return render(request,"userdonation.html")

def UserDonation(request):
    return render(request,"donated items.html")

def NgoHomePage(request):
    return render(request,"homepagelogin.html")

def about(request):
    return render(request,"about.html")

def NgoRequirement(request):
    equipments = Equipments.objects.all()
    equi_dict = {'Equipments': equipments}
    return render(request,"request.html",equi_dict)

def DonateUser(request):
    equipments = Equipments.objects.all()
    equi_dict = {'Equipments': equipments}
    return render(request, "donation.html", equi_dict)