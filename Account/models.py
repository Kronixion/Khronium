from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    age = models.IntegerField()
    token = models.CharField(max_length=100,blank=True, null=True, default="")
    loginAttempt = models.IntegerField(default=0)
    lockoutDateTime = models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
        return self.user.username