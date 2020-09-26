from django import forms

class CreateUser(forms.Form):
    fname = forms.CharField(label='fname',max_length=30)
    lname = forms.CharField(label='fname',max_length=30)
    email = forms.EmailField()
    phone = forms.IntegerField()
    password1 = forms.CharField(max_length=25, widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=25, widget=forms.PasswordInput)
    Address = forms.CharField(widget=forms.Textarea(),max_length=300)
    country = forms.CharField(max_length=50)
    pincode = forms.IntegerField()
    def clean(self):
        if self.password1 != self.password2:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )

class NgoUser(forms.Form):
    ngo_name = forms.CharField(max_length=50)
    ngo_email = forms.EmailField()
    ngo_phone = forms.IntegerField()
    ngo_pass1 = forms.CharField(max_length=25,widget=forms.PasswordInput)
    ngo_pass2 = forms.CharField(max_length=25, widget=forms.PasswordInput)
    Address = forms.CharField(widget=forms.Textarea(),max_length=300)
    Country = forms.CharField(max_length=50)
    pincode = forms.IntegerField()
    weblink = forms.URLField()

<<<<<<< HEAD
=======

>>>>>>> 40863d9128ad2a553ff540cf43a501a9e96fc179
