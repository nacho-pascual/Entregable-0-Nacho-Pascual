import requests
import time
import csv
import matplotlib.pyplot as plt
import operator
import os
import errno
import shutil



palabras={}
def timer():
  while True:
    
    respuesta =requests.get('https://thesimpsonsquoteapi.glitch.me/quotes')
    frase=respuesta.json()[0]['quote']
    personaje=respuesta.json()[0]['character']
    imagen=respuesta.json()[0]["image"]
    print(frase)
    print(personaje)
    
    try:
      os.mkdir(f'BartSimpson/{personaje}')
    except OSError as e:
      if e.errno != errno.EEXIST:
        raise
   
    url = imagen
    nombreImagen = "BartSimpson/" + personaje +"/"+personaje+".png"
    r = requests.get(imagen, stream=True)
    with open(nombreImagen, 'wb') as f:
        r.raw.decode_content = True
        shutil.copyfileobj(r.raw, f)

    simbolos = ['¿','?','.','.',';',':','¡','!','"',',']
    for simbolo in simbolos:
      frase = frase.replace(simbolo,' ')
    palabras_frase = ((frase.lower()).title()).split()
    print(palabras_frase)
    for palabra in palabras_frase:
      palabras[palabra] = palabras.get(palabra , 0) + 1    
      
    for key in palabras:
      if palabras[key] == 1:
        veces = 'vez'
      else:
        veces='veces'
      
      print(f'La palabra {key} se ha repetido {palabras[key]} {veces}')
    
    palabras_odenado = dict(sorted(palabras.items(), key=operator.itemgetter(1), reverse=True)[:10])


    with open('BartSimpson/contador.csv', 'w', newline='') as file:
        fieldnames=['Palabras','N de repeticiones']
        writer=csv.DictWriter(file,fieldnames=fieldnames)
        if file.tell() == 0:
          writer.writeheader()
        for key in palabras:
          writer.writerow({'Palabras':key,'N de repeticiones':palabras[key]}) 


    time.sleep(3) 
timer()
