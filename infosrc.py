import pandas as pd
import requests
from pandas.io.json import json_normalize
import json

class Fetchdf():
    """docstring for Fetch."""
    def __init__(self):
        #self.arg = arg super().__init__(**kwds)
        
        self.url = "https://api.nal.usda.gov/fdc/v1/foods/search?query=plantain&dataType=SR%20Legacy&pageSize=2&api_key=DEMO_KEY"
#df = pd.read_json(url)
        self.df=self.framedata(self.url)
    
    def framedata(self,src):
        data=json.loads(requests.get(src).text)
        df = pd.json_normalize(data['foods'],['foodNutrients'], ['fdcId','description'],errors='ignore')
        return df
