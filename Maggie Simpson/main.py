import requests
import time
import csv


def timer():
  while True:
    respuesta = requests.get('https://thesimpsonsquoteapi.glitch.me/quotes')
    frase=respuesta.json()[0]['quote']
    personaje=respuesta.json()[0]['character']
    print(frase)
    print(personaje)
    time.sleep(3) 
    
    data={"quote":frase,"character":personaje}
    if personaje == 'Homer Simpson':
      with open('Maggie Simpson/Homer/mycsvfile.csv', 'a', newline='') as f:
        a=csv.DictWriter(f,data.keys())
        a.writerow(data) 
    elif personaje == 'Lisa Simpson':
      with open('Maggie Simpson/Lisa/mycsvfile.csv', 'a', newline='') as g: 
        a=csv.DictWriter(g,data.keys())
        a.writerow(data)
    else:
      with open('Maggie Simpson/General/mycsvfile.csv', 'a', newline='') as h: 
        a=csv.DictWriter(h,data.keys())
        a.writerow(data)

timer()



