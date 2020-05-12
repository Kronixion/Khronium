#Django imports
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

# Forms
from .forms import NewBoard

# Models
from Account.models import Account
from .models import ProjectBoard

@login_required
def boards(request):
    account = Account.objects.get(user = request.user)
    form = NewBoard()
    try: 
        projectBoards = ProjectBoard.objects.filter(account=account)
    except ProjectBoard.DoesNotExist:
        projectBoards = None
    print(projectBoards)
    print("Project Boards : " + str(projectBoards))
    return render(request,'boards.html',{'form':form,'boards':projectBoards})

@login_required
def addBoard(request):
    account = Account.objects.get(user = request.user)
    if request.method == "POST":
        form = NewBoard(request.POST)
        if form.is_valid():
            board = form.save(commit=False)
            board.account = account
            board.save()
            return redirect('/boards/')
        else:
            return redirect('/boards/')
    else:
        return redirect('/boards/')

@login_required
def viewBoard(request,id):
    return render(request,'projectBoards.html')

@login_required
def addList(request):
    pass

@login_required
def addItem(request):
    pass