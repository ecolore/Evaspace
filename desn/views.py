from django.shortcuts import render
from .models import Collection

def latest(request): 
 collections = Collection.objects.all()
 return render(request, 'asset/intro.htm', {'collections': collections})
