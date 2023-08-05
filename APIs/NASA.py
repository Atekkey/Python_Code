import pip._vendor.requests
from datetime import date
from urllib.request import urlretrieve
from pprint import PrettyPrinter
pp = PrettyPrinter()
today = date.today()

apiKey = 'bskLOqQep8cnRWdAuU5ifXdqgDh04DyilbaV7YaO'

def fetchAPOD():
  URL_APOD = "https://api.nasa.gov/planetary/apod"
  date = '2020-01-22'
  params = {'api_key':apiKey, 'date':today, 'hd':'True'}
  response = pip._vendor.requests.get(URL_APOD,params=params).json()
  pp.pprint(response)
  print("\nHD URL = " + response.get('hdurl') + "\n")
fetchAPOD()
