from django import forms

class CreateUser(forms.Form):
    fname = forms.CharField()
    lname = forms.CharField()
    email = forms.EmailField()
    phone = forms.IntegerField()
    password = forms.CharField()
    Address = forms.TextField()
    country = forms.CharField()
    pincode = forms.IntegerField()

class NgoUser(forms.Form):
    ngo_name = forms.CharField()
    ngo_email = forms.EmailField()
    ngo_phone = forms.IntegerField()
    ngo_pass = forms.CharField()
    Address = forms.TextField()
    Country = forms.CharField()
    pincode = forms.IntegerField()
    weblink = forms.URLField()

<<<<<<< HEAD
=======
class
>>>>>>> 487ca19e8c20a87f1d8d8636f89e8bca7d7c3e2e
