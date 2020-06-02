from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Account

class ExtendedUserCreationForm(UserCreationForm):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class':'form-control fadeIn first','placeholder':'Username'}))
    email = forms.EmailField(required = True, widget=forms.TextInput(attrs={'class':'form-control fadeIn second','placeholder':'E-mail'}))
    first_name = forms.CharField(max_length=30, required = True, widget=forms.TextInput(attrs={'class':'form-control fadeIn third','placeholder':'First Name'}))
    last_name = forms.CharField(max_length=30, required = True, widget=forms.TextInput(attrs={'class':'form-control fadeIn fourth','placeholder':'Last Name'}))
    password1 = forms.CharField(required = True, widget=forms.PasswordInput(attrs={'class':'form-control fadeIn sixth','placeholder':'Password'}))
    password2 = forms.CharField(required = True, widget=forms.PasswordInput(attrs={'class':'form-control fadeIn seventh','placeholder':'Confirm Password'}))

    class Meta:
        model = User
        fields = ('username','email','first_name','last_name','password1','password2')

class AccountForm(forms.ModelForm):
    age = forms.IntegerField(required = True, widget=forms.TextInput(attrs={'class':'form-control fadeIn fifth','placeholder':'Age'}))

    class Meta():
        model = Account
        fields = ('age',)

class AccountSignInForm(forms.Form):
    username = forms.CharField(required=True,max_length=150, widget=forms.TextInput(attrs={'class':'form-control fadeIn first','placeholder':'Username'}))
    password = forms.CharField(required=True,widget = forms.PasswordInput(attrs={'class':'form-control fadeIn second','placeholder':'Password'}))

class ResetPassword(forms.Form):
    email = forms.CharField(required=True, widget = forms.TextInput(attrs={'class':'form-control','placeholder':'E-mail'}))

class ResetPasswordConfirmation(forms.Form):
    password = forms.CharField(required=True, widget = forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}))
    passwordConfirm = forms.CharField(required=True,widget = forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password Confirmation'}))
