from django.db import models

class TimeStampedModel(models.Model):
    created = models.DateTimeField("criado em", auto_now=True, auto_now_add=False)
    modified = models.DateTimeField("Modificado em", auto_now=False, auto_now_add=True)
    
    class Meta:
        abstract = True