from flask import Flask
from threading import Thread
from random import choice

app = Flask('')

quote = ["Never gonna give you up",  "And never gonna let you down", "I don't know what am I doing", "🤔"]

@app.route('/')
def home():
	return """
    <h1 style='color: black; font-family: monospace;'>NongKanoon</h1>
    <p>{p}</p>
		<img src="https://images.unsplash.com/photo-1523567353-71ea31cb9f73?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1050&q=80" alt="dog" width=70%>
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