from django.db import models
from Account.models import Account

class ProjectBoard(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=100,default="")
    creationDate = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
    
class UnorderedList(models.Model):
    dashboard = models.ForeignKey(ProjectBoard, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Item(models.Model):
    unorderedList = models.ForeignKey(UnorderedList, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text