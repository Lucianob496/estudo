from fastapi import FastAPI
import sqlite3
import requests

conn = sqlite3.connect('songs.sqlite3',check_same_thread=False) 
c = conn.cursor()

app = FastAPI()

@app.get("/artist")
def procura(key):
  a = c.execute('''SELECT anime FROM Songs WHERE artist LIKE ? ORDER BY RANDOM() LIMIT 1''', (key,))
  return a.fetchone()
