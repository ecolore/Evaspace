from django.conf import settings 
from django.db import models
from datetime import datetime
from django.urls import reverse

def EP():
 #import datetime
 d2=datetime.date.today()
 open=datetime.date(2021,3,1)
'''print((d2.isocalendar()[1]-9)*5)
print(d2.weekday()+1) 
.strftime('%V'))'''

class Collection(models.Model):
    """A typical class defining a model, derived from the Model class."""
    '''Fields <3 顏色比❤️溫和'''
    dt_str=models.CharField(max_length=8,verbose_name='date',default=datetime.now().strftime('%y%m%d'))
    dthour_section = models.CharField(max_length=15, default=datetime.now().strftime('%m%d%H'+'-'+'%M'), primary_key=True)
    pop_hms = models.CharField(max_length=8, default=datetime.now().strftime('%H:%M:%S'))
    title=models.CharField(max_length=30)
    artist=models.CharField(max_length=24)
    note=models.CharField(max_length=10,blank=True)
    sysdate=models.DateTimeField(auto_now_add=True)

objects = models.Manager() # MANAGERS 
 

    # Metadata
class Meta:
  indexes = [models.Index(fields=['dthour_section'])]
      #  ordering = ['-dt_str']

    # Methods
  def get_absolute_url(self):
        """Returns the url to access a particular instance of Collection."""
        return reverse('view_latest', kwargs={'pk':str(self.id)})

  def __str__(self):
        """String for representing the Collection object (in Admin site etc.)."""
        return self.dt_str
