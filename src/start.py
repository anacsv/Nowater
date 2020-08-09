import requests
import json
from datetime import datetime

# URl da API da Sanepar
url = 'https://services1.arcgis.com/46Oage49MS2a3O6A/arcgis/rest/services/Mapa_Rodizio_Abastecimento_RMC_View/FeatureServer/2/query?f=json&where=CODOPE%3D%2700041%27&returnGeometry=false&spatialRel=esriSpatialRelIntersects&outFields=OBJECTID%2CRETOMADA%2CNORMALIZACAO%2CLOCALIDADE%2CPERIODO%2COBSERVACAO%2CINICIO%2CCODOPE'
get_info = requests.get(url)
resp = get_info.json()


def formatDateTime(dt):
  return datetime.utcfromtimestamp(int(dt)/1000).strftime('%d/%m/%Y %H:%M')


for item in resp['features']:
   print(f"""Início do rodízio: {formatDateTime(item['attributes']['INICIO'])}
Previsão de volta entre: {formatDateTime(item['attributes']['RETOMADA'])} e {formatDateTime(item['attributes']['NORMALIZACAO'])} """)




