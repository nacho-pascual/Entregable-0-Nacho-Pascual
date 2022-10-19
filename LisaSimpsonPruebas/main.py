import requests
import time
import csv
import os
import errno
import ntpath
import shutil

palabras={}
def timer():
  while True:
    respuesta = requests.get('https://thesimpsonsquoteapi.glitch.me/quotes')
    frase=respuesta.json()[0]['quote']
    personaje=respuesta.json()[0]['character']
    imagen=respuesta.json()[0]["image"]
    print(frase)
    print(personaje)


    try:
      os.mkdir(f'LisaSimpsonPruebas/{personaje}')
    except OSError as e:
      if e.errno != errno.EEXIST:
        raise
   
    url = imagen

    r = requests.get(imagen, stream=True)
    if personaje== ntpath.basename(personaje):
      with open(f'LisaSimpsonPruebas/{personaje}/imagen.png', 'wb') as f:
          r.raw.decode_content = True
          shutil.copyfileobj(r.raw, f)      


    simbolos = ['¿','?','.','.',';',':','¡','!']
    for simbolo in simbolos:
      x=frase.title()
      x = x.replace(simbolo,' ')
    palabras_frase = x.split()
    print(palabras_frase)
    for palabra in palabras_frase:
      palabras[palabra] = palabras.get(palabra , 0) + 1    
      
    for key in palabras:
      if palabras[key] == 1:
        veces = 'vez'
      else:
        veces='veces'
      
      #print(f'La palabra {key} se ha repetido {palabras[key]} {veces}')
    with open('LisaSimpsonPruebas/contador.csv', 'w', newline='') as file:
      fieldnames=['Palabras','N de repeticiones']
      writer=csv.DictWriter(file,fieldnames=fieldnames)
      if file.tell() == 0:
        writer.writeheader()
      for key in palabras:
        writer.writerow({'Palabras':key,'N de repeticiones':palabras[key]}) 


    data={"quote":frase,"character":personaje}
    if personaje== ntpath.basename(personaje):
      with open(f'LisaSimpsonPruebas/{personaje}/mycsv.csv', 'a', newline='') as f:
        a=csv.DictWriter(f,data.keys())
        a.writerow(data) 
    
timer()



