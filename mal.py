import requests
from collections import Counter


client_id = ''


lista = []
lista1 = []
lista2 = []

usuarios = []

usuarios_anilist = []

total = len(usuarios) + len(usuarios_anilist)

duplicado = []


query = '''
query ($userName: String) { # Define which variables will be used in the query (id)
    MediaListCollection (userName: $userName, type: ANIME, status: PLANNING, status_in: [PLANNING]) { # Insert our variables into the query arguments (id) (type: ANIME is hard-coded in the query)
    lists{
        entries{
            media{
                title{
                    romaji
                }
            }
        }
    }
  }
}
'''
url2 = 'https://graphql.anilist.co'

for x in usuarios_anilist:
    if len(usuarios_anilist) == 0:
      pass

    else:
      variables = {
          'userName': f'{x}'
              }

      response = requests.post(url2, json={'query': query, 'variables': variables})

      lista1 = response.json()['data']['MediaListCollection']['lists'][0]['entries']

      for i in lista1:
        lista2.append((i['media']['title']['romaji']))




for i in usuarios:
    if len(usuarios) == 0:
      pass
    else:
      url = f'https://api.myanimelist.net/v2/users/{i}/animelist?fields=list_status&limit=1000&status=plan_to_watch'

      response = requests.get(url, headers = {
      'X-MAL-CLIENT-ID': client_id
      })

      anime_list = response.json()

      lista = anime_list['data']

      for i in anime_list['data']:
          lista2.append(i['node']['title'])


response.close()

contado = []

for i,j in Counter(lista2).items():
    if j >= 2:
        duplicado.append(i)
        contado.append((i,j))

for y in contado:
  print(y)
