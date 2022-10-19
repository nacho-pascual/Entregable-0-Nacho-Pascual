import requests
import time
import csv
import shutil



def timer():
  while True:
    respuesta = requests.get('https://thesimpsonsquoteapi.glitch.me/quotes')
    frase=respuesta.json()[0]['quote']
    personaje=respuesta.json()[0]['character']
    imagen=respuesta.json()[0]["image"]
    print(frase)
    print(personaje)
    print(imagen)
    url = imagen

    r = requests.get(imagen, stream=True)
    with open(f'LisaSimpson/General/{personaje}.png', 'wb') as f:
        r.raw.decode_content = True
        shutil.copyfileobj(r.raw, f)

    data={"quote":frase,"character":personaje}
    if personaje == 'Homer Simpson':
      with open('LisaSimpson/Homer/mycsvfile.csv', 'a', newline='') as f:
        a=csv.DictWriter(f,data.keys())
        a.writerow(data) 
    elif personaje == 'Lisa Simpson':
      with open('LisaSimpson/Lisa/mycsvfile.csv', 'a', newline='') as g: 
        a=csv.DictWriter(g,data.keys())
        a.writerow(data)
    else:
      with open('LisaSimpson/General/mycsvfile.csv', 'a', newline='') as h: 
        a=csv.DictWriter(h,data.keys())
        a.writerow(data)

timer()



