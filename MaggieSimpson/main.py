#Importamos las librerias necesarias
import requests
import time
import csv


def timer():
  while True:
    #Obtenemos los datos de la App
    respuesta = requests.get('https://thesimpsonsquoteapi.glitch.me/quotes')
    frase=respuesta.json()[0]['quote']
    personaje=respuesta.json()[0]['character']
    print(frase)
    print(personaje)
    time.sleep(1) 
    #Generamos un csv con las frases de todos los personajes 
    data={"quote":frase,"character":personaje}
    with open('MaggieSimpson/General/General.csv', 'a', newline='') as h: 
      a=csv.DictWriter(h,data.keys())
      a.writerow(data)
    
    #Generamos un csv con las frases de Homer Simpson 
    if personaje == 'Homer Simpson':
      with open('MaggieSimpson/Homer/Homer.csv', 'a', newline='') as f:
        a=csv.DictWriter(f,data.keys())
        a.writerow(data) 
    
    #Generamos un csv con las frases de Homer Simpson 

    elif personaje == 'Lisa Simpson':
      with open('MaggieSimpson/Lisa/Lisa.csv', 'a', newline='') as g: 
        a=csv.DictWriter(g,data.keys())
        a.writerow(data)
    
     
timer()



