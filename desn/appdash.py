import dash
import dash_table
from infosrc import Fetchdf
# import requests
# from pandas.io.json import json_normalize
# import json
#import pandas as pd

# url = ""
# r=requests.get(url)
# df = pd.json_normalize(r.json(),record_path=['foods'])
df=Fetchdf().df
app = dash.Dash(__name__)
app.layout = dash_table.DataTable(
    id='table',
    columns=[{"name": i, "id": i} for i in df.columns],
    data=df.to_dict('records'),
)

if __name__ == '__main__':
    app.run_server(debug=True)
