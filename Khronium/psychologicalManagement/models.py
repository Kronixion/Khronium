from django.db import models
from django.utils.translation import gettext_lazy as _
from Account.models import Account

class PsychologicalModel(models.Model):
    score = models.IntegerField()
    account = models.ForeignKey(Account,on_delete=models.CASCADE,blank=True, null=True)
    dateTaken = models.DateField(auto_now=True)

    class FormType(models.TextChoices):
        MADRS= 'MD', _('MADRS')
        KEDS= 'KD', _('KEDS')

    formType = models.CharField(max_length=2, choices=FormType.choices)