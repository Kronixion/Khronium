from django.shortcuts import render
from Account.models import Account
from .models import DailyList, Event
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from projectManagement.models import ProjectBoard, UnorderedList, Item

@login_required
def viewTimeManagement(request):
    account = Account.objects.get(user = request.user)
    dailyLists = DailyList.objects.filter(account=account).order_by('date')
    events = Event.objects.all().order_by('startTime')
    projectBoards = ProjectBoard.objects.filter(account=account)
    unorderedLists = UnorderedList.objects.all()
    items = Item.objects.all()
    return render(request,'timeManagement.html',{"dailyLists":dailyLists,"events":events,"unorderedLists":unorderedLists,"projectBoards":projectBoards,"items":items})

@login_required
def addDailyList(request):
    account = Account.objects.get(user = request.user)
    if request.method == "POST":
        try: 
            dailyList = DailyList.objects.get(date=request.POST["date"])
        except DailyList.DoesNotExist:
            dailyList = None
        if dailyList == None:
            dailyList = DailyList(account=account,date=request.POST["date"])
            dailyList.save()
            return HttpResponse(str(dailyList.id))
        else: 
            return HttpResponse(str(-1))
    else:
        return HttpResponse("Get Request")

@login_required
def removeDailyList(request):
    if request.method=="POST":
        dailyList = DailyList.objects.get(id=request.POST["id"])
        dailyList.delete()
        return HttpResponse("List Deleted")
    else:
        return HttpResponse("Get Request")

@login_required
def addEvent(request):

    if request.method=="POST":
        try:
            dailyList = DailyList.objects.get(id=request.POST['listId'])
        except DailyList.DoesNotExist:
            dailyList = None
        if dailyList != None:
            itemId = request.POST.get('itemId',False)
            if itemId == -1:
                event = Event(dailyList = dailyList, startTime=request.POST["startTime"], endTime=request.POST["endTime"], description=request.POST["description"])
                event.save()
                return HttpResponse(str(event.id))
            else:
                event = Event(dailyList = dailyList, startTime=request.POST["startTime"], endTime=request.POST["endTime"], description=request.POST["description"],itemId=itemId)
                event.save()
                return HttpResponse(str(event.id))
        else:
            return HttpResponse(str(-1))
    else:
        return HttpResponse("Get Request")

@login_required
def updateEvent(request):
    if request.method == 'POST':
        event = Event.objects.get(id=request.POST['eventId'])
        event.description = request.POST['description']
        event.save()
        if event.itemId != -1:
            item = Item.objects.get(id=event.itemId)
            item.text = request.POST['description']
            item.save()
        return HttpResponse("Success")
    else:
        return HttpResponse("Get Request")

@login_required
def removeEvent(request):
    if request.method == 'POST':
        event = Event.objects.get(id=request.POST['eventId'])
        event.delete()
        return HttpResponse("Deletion Successfull")
    else:
        HttpResponse("Get Request")

def moveProjectTaskToAnotherList(request):
    if request.method=="POST":
        unorderedList = UnorderedList.objects.get(id=request.POST["listId"])
        event = Event.objects.get(id=request.POST["projectTask"])
        item = Item.objects.get(id=event.itemId)
        item.unorderedList = unorderedList
        item.save()
        event.itemId = -1
        event.save()
        return HttpResponse("Success")