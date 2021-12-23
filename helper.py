from datetime import datetime
import requests
import json 
import pytz

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

def fetch(url):      
  res = requests.get(url)
  response = json.loads(res.text)
  return response

def printList(listname,l):
  print(listname)
  for x in l:
    print(x)
  print('-------------------')

def rateLimit():
  r = requests.head(url="https://discord.com/api/v1")
  print('-------------------')
  try:
    print(f"Rate limit {int(r.headers['Retry-After']) / 60} minutes left")
  except:
    print("No rate limit")
  print('-------------------')