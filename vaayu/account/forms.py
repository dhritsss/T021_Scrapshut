from django import forms

class CreateUser(forms.Form):
    fname = forms.CharField()
    lname = forms.CharField()
    email = forms.EmailField()
    phone = forms.IntegerField()
    password = forms.CharField()
    password2 = forms.CharField()
    Address = forms.CharField()

class NgoUser(forms.Form):
    pass