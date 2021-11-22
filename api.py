from datetime import datetime
import pytz
import requests
import json

def bangkok():
  return datetime.now(pytz.timezone('Asia/Bangkok'))

def dateColor():
  d = bangkok().strftime("%a")
  day = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
  colour = [
    0xf1c40f, 0xe91e63, 
    0x2ecc71, 0xe67e22, 
    0x3498db, 0x7289da
  ]
  return colour[day.index(d)]
  
def dateInfo():
  return bangkok().strftime("%a %d %b, %Y")
  #Fri 19 Nov, 2021

def requestAPI(url):
  responce = requests.get(url)
  json_data = json.loads(responce.text)
  return json_data