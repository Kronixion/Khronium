from django.db import models

class PsychologicalModel(models.Model):
    last_compelte = models.DateTimeField(auto_now=True)
    result = models.IntegerField()
    
    class FormType(models.TextChoices):
        MADRS= 'MD', _('MADRS')
        KEDS= 'KD', _('KEDS')

    formType = models.CharField(max_length=2, choices=FormType.choices)