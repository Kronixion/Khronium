from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Account
from .forms import AccountForm, ExtendedUserCreationForm, AccountSignInForm, ResetPassword, ResetPasswordConfirmation
from django.contrib.auth import authenticate, login, logout
from django.core import mail
from django.template.loader import render_to_string
from django.utils.crypto import get_random_string
from django.utils.html import strip_tags
from datetime import timedelta, datetime

def signUp(request):
    userForm = ExtendedUserCreationForm()
    accountForm = AccountForm()
    if request.method == "POST":
        userForm = ExtendedUserCreationForm(request.POST)
        accountForm = AccountForm(request.POST)
        if userForm.is_valid() and accountForm.is_valid():
            try:
                user = User.objects.get(email=request.POST['email'])
            except User.DoesNotExist:
                user = None
            print(user)
            if user == None:
                user = userForm.save()
                profile = accountForm.save(commit=False)
                profile.user = user
                profile.save()
                return redirect('/signIn/')
            else:
                context = {'userForm':userForm,'accountForm':accountForm,'message':'The email has been taken'}
                return  render(request,'signUp.html',context)
        else:
            print(userForm.errors)
            context = {'userForm':userForm,'accountForm':accountForm,'errors':userForm.errors}
            return  render(request,'signUp.html',context)
    else:
        context = {'userForm':userForm,'accountForm':accountForm}
        return  render(request,'signUp.html',context)

def signIn(request):
    form = AccountSignInForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                account = Account.objects.get(user=user)
                if account.lockoutDateTime is not None:
                    unlockTime = account.lockoutDateTime + timedelta(minutes=5)
                    unlockTime = unlockTime.replace(tzinfo=None)
                    print(unlockTime)
                    print(datetime.now())
                    if datetime.now() < unlockTime:
                        message = 'Yout account is locked, due to too many login attempts!'
                        return render(request, 'signIn.html',{'form':form,'message':message})
                    else:
                        account.loginAttempt = 0
                        account.lockoutDateTime = None
                account.token=''
                account.save()
                login(request, user)
                return redirect('/dashboard/')
                
            else:
                try:
                    user = User.objects.get(username=username)
                except User.DoesNotExist:
                    user = None

                if user is not None:
                    user = User.objects.get(username=username)
                    account = Account.objects.get(user=user)
                    account.loginAttempt += 1
                    if account.loginAttempt == 5:
                        account.lockoutDateTime = datetime.now()
                    account.save()
                    message = 'Wrong password!'
                    return render(request, 'signIn.html',{'form':form,'message':message})
                else:
                    message = 'Wrong username!'
                    return render(request, 'signIn.html',{'form':form,'message':message})
        else: 
            return render(request, 'signIn.html',{'form':form})
    else:
        return render(request, 'signIn.html',{'form':form})

def signOut(request):
    logout(request)
    return redirect('/')

def resetPassword(request):
    if request.method == "POST":
        user = User.objects.get(email = request.POST['email'])
        account = Account.objects.get(user = user)
        account.token = get_random_string(length=64)
        account.save()
        subject = 'Khronium - Reset Password'
        html_message = render_to_string('email_template.html',{'token':account.token})
        plain_message = strip_tags(html_message)
        from_email = 'From <khroniumwebsite@gmail.com>'
        to = request.POST['email']
        mail.send_mail(subject, plain_message, from_email, [to], html_message=html_message,fail_silently=False)
        return redirect('/')
    else:
        form = ResetPassword()
        return render(request,"resetPassword.html",{"form":form})

def resetPasswordConfirm(request,token):
    try:
        account = Account.objects.get(token=token)
    except Account.DoesNotExist:
        return render(request,'resetPasswordConfirmation.html',{'message':'Token hase expired!','token':token,'expired':True})
    if request.method == 'POST':
        if request.POST['password'] == request.POST['passwordConfirm']:
            account.user.set_password(request.POST['password'])
            account.token=''
            account.user.save()
            account.save()
            return redirect('signIn')
        else:
            form = ResetPasswordConfirmation()
            return render(request,'resetPasswordConfirmation.html',{'message':'The passwords don\'t match.','token':token,'form':form})
    else:
        form = ResetPasswordConfirmation()
        return render(request,'resetPasswordConfirmation.html',{'form':form,'token':token})