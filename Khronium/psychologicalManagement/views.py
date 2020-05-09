from django.shortcuts import render, redirect
from .models import PsychologicalModel
from Account.models import Account
from .forms import KEDSForm, MADRSForm
from django.contrib.auth.decorators import login_required
from datetime import timedelta, date

@login_required
def psychologicalDashboard(request):
    account = Account.objects.get(user=request.user)
    kedsResults = PsychologicalModel.objects.filter(account=account, formType='KD')
    madrsResults = PsychologicalModel.objects.filter(account=account, formType='MD')
    if madrsResults.last() == None:
        madrsMostRecentResult = None
    else:
        madrsMostRecentResult = madrsResults.last().dateTaken+timedelta(days=7)
    if kedsResults.last() == None:
        kedsMostRecentResult = None
    else:
        kedsMostRecentResult = kedsResults.last().dateTaken+timedelta(days=7)
    return render(request,'psychologicalManagement.html',{'kedsResults':kedsResults,'madrsResults':madrsResults,'madrsMostRecentResult':madrsMostRecentResult,'kedsMostRecentResult':kedsMostRecentResult})

@login_required
def madrs(request):
    account = Account.objects.get(user=request.user)
    madrsMostRecentResult = PsychologicalModel.objects.filter(account=account, formType='MD').last()
    if madrsMostRecentResult == None or date.today() > madrsMostRecentResult.dateTaken+timedelta(days=7):
        if request.method == "POST":
            formScore = 0
            for value in request.POST.values():
                if len(value)==1:
                    formScore += int(value)
            psychologicalModel = PsychologicalModel(account=account,score=formScore,formType='MD')
            psychologicalModel.save()
            return render(request,'resultPage.html',{'formType':'MD','result':formScore})
        else:
            madrsForm = MADRSForm()
            return render(request, 'madrs.html',{'madrsForm':madrsForm})
    else:
        return redirect('/psychologicalDashboard/')

@login_required
def keds(request):
    account = Account.objects.get(user=request.user)
    kedsMostRecentResult = PsychologicalModel.objects.filter(account=account, formType='KD').last()
    if kedsMostRecentResult == None or date.today() > kedsMostRecentResult.dateTaken+timedelta(days=7):
        if request.method == "POST":
            formScore = 0
            for value in request.POST.values():
                if len(value)==1:
                    formScore += int(value)
            psychologicalModel = PsychologicalModel(account=account,score=formScore,formType='KD')
            psychologicalModel.save()
            return render(request,'resultPage.html',{'formType':'KD','result':formScore})
        else:
            kedsForm = KEDSForm()
            return render(request, 'keds.html',{'kedsForm':kedsForm})
    else:
        return redirect('/psychologicalDashboard/')