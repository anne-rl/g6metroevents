from django import forms
from .models import *
            
class UserForm(forms.ModelForm):
   
       class Meta:
           model = User
           fields = ['userName','firstName']

            
class EventForm(forms.ModelForm):
   
       class Meta:
           model = Event
           fields = ['eventName','description']