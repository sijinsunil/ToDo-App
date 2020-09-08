from django import forms
from django.forms import ModelForm

from .models import *

class Task_todoForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Add new to do..'}))
    notes = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Something about to do..'}))
    
    class Meta:
        model = Task_todo
        fields ='__all__'