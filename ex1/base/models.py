'''
ass
'''

from django.db import models

# Create your models here.

class Task_todo(models.Model):
    title = models.CharField(max_length=200)
    notes = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title