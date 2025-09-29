# Baixar as musicas e escrever metadados de uma lista gerada por script do animemusicquiz

import json
from urllib.request import urlretrieve
import shutil
import eyed3

eyed3.log.setLevel("ERROR")


f = open('lista.json') # retirado do script https://github.com/joske2865/AMQ-Scripts/raw/master/amqSongListUI.user.js

data = json.load(f)

for i in data:
  print((i['anime']['romaji'], 'https://naedist.animemusicquiz.com/' + i['urls']['catbox']['0']))
  
  urlretrieve('https://naedist.animemusicquiz.com/' + i['urls']['catbox']['0'], 'musicas/' + i['anime']['romaji'] + ' ' + i['type'] + ' ' + i['name'] +'.mp3')
  
  audiofile = eyed3.load('musicas/' + i['anime']['romaji'] + ' ' + i['type'] + ' ' + i['name'] +'.mp3')
  
  if not audiofile.tag:
    audiofile.initTag()
  
  audiofile.tag.artist = i['artist']
  
  audiofile.tag.album = i['anime']['romaji']
  
  audiofile.tag.title = i['name']
  
  audiofile.tag.save()

shutil.make_archive('coloca o nome do zip aqui', 'zip', 'musicas')
