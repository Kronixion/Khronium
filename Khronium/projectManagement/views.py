#Django imports
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# Forms
from .forms import NewBoard

# Models
from Account.models import Account
from .models import ProjectBoard, UnorderedList, Item

@login_required
def boards(request):
    print("Redirected")
    account = Account.objects.get(user = request.user)
    form = NewBoard()
    try: 
        projectBoards = ProjectBoard.objects.filter(account=account)
    except ProjectBoard.DoesNotExist:
        projectBoards = None
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

def updateBoard(request):
    if request.method == "POST":
        title = request.POST['title']
        description = request.POST['description']
        board = ProjectBoard.objects.get(id=request.POST['boardId'])
        print(board)
        board.title = title
        board.description = description
        board.save()
        return HttpResponse("1")
    else:
        return HttpResopnse("0")

def deleteBoard(request):
    print(request.POST)
    if request.method == "POST":
        board = ProjectBoard.objects.filter(id=request.POST['boardId'])
        board.delete()
        return redirect('/boards/')
    else:
        return redirect('/boards/')

@login_required
def viewBoard(request,id):
    board = ProjectBoard.objects.get(id=id)

    try:
        unorderedList = UnorderedList.objects.filter(dashboard=board)
    except UnorderedList.DoesNotExist:
        unorderedList = None

    
    return render(request,'projectBoards.html',{'board':board,'lists':unorderedList})

@login_required
def addList(request,id):
    board = ProjectBoard.objects.get(id=id)
    if request.method == 'POST' and request.POST['listName'] != "":
        unorderedList = UnorderedList(dashboard=board, title=request.POST['listName'])
        unorderedList.save()
        return redirect('viewBoard',id=id)
    else:
        return redirect('viewBoard',id=id)

@login_required
def addItem(request,id):
    if request.method=="POST":
        unorderedList = UnorderedList.objects.get(id=request.POST[id])
        item = Item(unorderedList=unorderedList, text=request.POST['itemText'])
        return redirect('viewBoard',id=id)
    else:
        return redirect('viewBoard',id=id)