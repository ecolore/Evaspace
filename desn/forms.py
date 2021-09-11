from django import forms
from django.forms import ModelForm
from .models import Collection

class FirstForm(ModelForm):
    class Meta:
        model = Collection
        fields ='__all__' #['title','artist']
        
#form=FirstfForm()    
#qry=forms.CharField()
