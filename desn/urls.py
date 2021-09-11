from django.conf.urls import url #path 
from . import views 
app_name = 'desn' 
urlpatterns = [ url(r'^/$', views.clasFormView.as_view()),] # change how we reference the new view. ]

#urlpatterns = [ path('', views.latest, name='view_latest'),]
