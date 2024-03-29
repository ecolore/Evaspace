from django.urls import resolve 
from django.test import TestCase 
from .views import latest
from django.urls import reverse 
class HomeTests(TestCase): 
   def test_home_view_status_code(self): 
     url = reverse('views_latest')
     response = self.client.get(url)
     self.assertEquals(response.status_code, 200)
   def test_home_url_resolves_home_view(self):
     view = resolve('/')
     self.assertEquals(view.func, home)
