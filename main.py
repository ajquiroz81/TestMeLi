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


#Conexión a la base de datos

import mysql.connector
import sys
import boto3
import os

ENDPOINT="users_database.123456789012.us-east-1.rds.amazonaws.com"
PORT="3306"
USER="jane_doe"
REGION="us-east-1"
DBNAME="users_database"
os.environ['LIBMYSQL_ENABLE_CLEARTEXT_PLUGIN'] = '1'

#gets the credentials from .aws/credentials
session = boto3.Session(profile_name='default')
client = session.client('rds')

token = client.generate_db_auth_token(DBHostname=ENDPOINT, Port=PORT, DBUsername=USER, Region=REGION)

try:
    conn =  mysql.connector.connect(host=ENDPOINT, user=USER, passwd=token, port=PORT, database=DBNAME, ssl_ca='SSLCERTIFICATE')
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS users (fec_alta, user_name, codigo_zip, credit_card_num, credit_card_ccv, cuenta_numero, direccion, geo_latitud, geo_longitud, color_favorito, foto_dni, ip, auto, auto_modelo, auto_tipo, auto_color, cantidad_compras_realizadas, avatar, fec_birthday, id)')
    conn.commit()
# Crea la tabla con los datos requeridos en la base de
df.to_sql('users', conn, if_exists='replace', index = False)