from urllib.request import urlopen
import requests
import json
import pandas as pd
from pandas import json_normalize
from sqlalchemy import create_engine
import pymysql
url="https://62433a7fd126926d0c5d296b.mockapi.io/api/v1/usuarios"
response = urlopen(url)
data_json = json.loads(response.read())
df = pd.DataFrame.from_dict(data_json)
engine = create_engine('sqlite://' , echo=True)
df.to_sql('users' , con=engine)