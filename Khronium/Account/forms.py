from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Account

class ExtendedUserCreationForm(UserCreationForm):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(required = True, widget=forms.TextInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=30, required = True, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=30, required = True, widget=forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(required = True, widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(required = True, widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('username','email','first_name','last_name','password1','password2')

class AccountForm(forms.ModelForm):
    age = forms.IntegerField(required = True, widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta():
        model = Account
        fields = ('age',)

class AccountSignInForm(forms.Form):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget = forms.PasswordInput(attrs={'class':'form-control'}))