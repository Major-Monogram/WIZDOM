from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def main():
  return "Bot is Ready to Server"

def run():
  app.run(host="0.0.0.0", port=0000)

def keep_alive():
  server = Thread(target=run)
  server.start()