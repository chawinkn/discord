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
  <div style="text-align: center;margin: 30px;">
    <h1 style='color: black; font-family: monospace;'>NongKanoon</h1>
    <p>{p}</p>
		<img src="https://f.ptcdn.info/114/052/000/os8vamgl4TQdXXSm2iI-o.jpg" alt="Deaw Kor Chin Eaen Lae Ka" width=30%>
    <h2><a href="https://discord.com/oauth2/authorize?client_id=826804870094127140&permissions=536804850935&scope=bot">Invite to discord</a></h2>
  </div>
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