from django import forms
from shop.models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
class contactform(forms.ModelForm):
    class Meta:
        fields='__all__'
        model=contact

class signupform(UserCreationForm):
    class Meta:
        fields=('first_name','last_name','email','username','password1','password2')
        model=User

class reviewform(forms.ModelForm):
    class Meta:
        fields='__all__'
        model=review