from django import forms
from .models import *

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email','password')

class DonarForm(forms.ModelForm):
    class Meta:
        model = Donar
        fields = '__all__'

class NGOForm(forms.ModelForm):
    class Meta:
        model = NGO
        fields = '__all__'
