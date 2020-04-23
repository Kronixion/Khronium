from django.shortcuts import render, redirect
from .models import Account
from .forms import AccountForm, ExtendedUserCreationForm, AccountSignInForm
from django.contrib.auth import authenticate, login, logout

def signUp(request):
    if request.method == "POST":
        userForm = ExtendedUserCreationForm(request.POST)
        accountForm = AccountForm(request.POST)
        print(userForm.is_valid())
        print(accountForm.is_valid())
        if userForm.is_valid() and accountForm.is_valid():
            user = userForm.save()
            profile = accountForm.save(commit=False)
            profile.user = user
            profile.save()
            return redirect('/signIn/')
    else:
        userForm = ExtendedUserCreationForm()
        accountForm = AccountForm()
    context = {'userForm':userForm,'accountForm':accountForm}
    return  render(request,'signUp.html',context)

def signIn(request):
    if request.method == 'POST':
        form = AccountSignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            print(user)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                return render(request, 'signIn.html',{'form':form})
        else: 
            return render(request, 'signIn.html',{'form':form})
    else:
        form = AccountSignInForm() 
        return render(request, 'signIn.html',{'form':form})

def signOut(request):
    logout(request)
    return redirect('/')