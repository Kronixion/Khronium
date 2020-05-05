from django.shortcuts import render
from django.contrib.auth.decorators import login_required
def landingPage(request):
    return render(request,'landingPage.html')

def additionalInfo(request):
    return render(request,'additionalInfo.html')

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')