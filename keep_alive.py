from flask import Flask
from threading import Thread
from random import choice

app = Flask('')

quote = ["Never gonna give you up",  "And never gonna let you down", "I don't know what am I doing", "🤔"]

@app.route('/')
def home():
	return """
  <title>NongKanoon</title>
  <link rel="icon" href="https://tokanoon.chawinkn.repl.co/icon/kn2.png" type="image/x-icon">
  <h1 style='color: black; font-family: monospace;'>NongKanoon</h1>
  <p>{p}</p>
	<img src="https://cataas.com/cat" alt="cat">
    """.format(p = choice(quote))
	# return choice(quote)

@app.route('/heyo')
def heyo():
  return "heyo"

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
  t = Thread(target=run)
  t.start()