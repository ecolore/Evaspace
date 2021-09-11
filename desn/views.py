from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
from django.http import HttpResponse
from django.views import View # import the View parent class 
from datetime import datetime
from .forms import FirstForm
from .models import Collection
from . import appdash

class clasFormView(FormView):
    form_class = FirstForm
    template_name = 'base.html' # add a template_name attribute # change the get method to get_context_data 

    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        context['now'] = datetime.now() 
        return context

    def get(self, request): 
        now = datetime.now() 
        html = "<html><body>It is now {}</body></html>".format(now) 
        return HttpResponse(html)

'''   from pandas.io.json import json_normalize
    import json

    url = "https://api.nal.usda.gov/fdc/v1/foods/search?api_key=DEMO_KEY&query=sweet%20potato"
    r=requests.get(url)
    df = pd.json_normalize(r.json(),record_path=['foods'])
    return df'''

def latest(request): 
    collections = Collection.objects.all()
    return render(request, 'asset/intro.htm', {'collections': collections})
