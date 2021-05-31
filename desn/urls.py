from django.urls import path 
from . import views 
app_name = 'desn' 
urlpatterns = [ path('', views.latest, name='latest'),]
