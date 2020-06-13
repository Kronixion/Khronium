from django.db import models
from Account.models import Account

class DailyList(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    date = models.DateField()
    
    def __str__(self):
        return str(self.date)

class Event(models.Model):
    dailyList = models.ForeignKey(DailyList, on_delete=models.CASCADE)
    startTime = models.TimeField(blank=True, null=True)
    endTime = models.TimeField(blank=True, null=True)
    itemId = models.IntegerField(blank=True, null=True, default=-1)
    description = models.CharField(max_length=200)

    def __str__(self):
        return str(self.startTime) + " " + str(self.endTime) + " " + str(self.description) 
