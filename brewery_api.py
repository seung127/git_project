import requests
import pandas as pd

url = 'https://api.openbrewerydb.org/v1/breweries'

response = requests.get(url)
res = response.json()
df = pd.json_normalize(res)

df.head()