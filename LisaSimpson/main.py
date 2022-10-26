import requests
import time
import csv
import os
import errno
import shutil

palabras={}
def timer():
  while True:
    #Obtenemos los datos de la App y (añadimos el dato de la imagen respecto a maggie)
    respuesta = requests.get('https://thesimpsonsquoteapi.glitch.me/quotes')
    frase=respuesta.json()[0]['quote']
    personaje=respuesta.json()[0]['character']
    imagen=respuesta.json()[0]["image"]
    #print(frase)
    #print(personaje)

     #Creamos un nuevo directorio por cada personaje
    try:
      os.mkdir(f'LisaSimpson/{personaje}')
    except OSError as e:
      if e.errno != errno.EEXIST:
        raise
    #Metemos cada imagen en su carpeta
    url = imagen
    nombreImagen = "LisaSimpson/" + personaje +"/"+personaje+".png"
    r = requests.get(imagen, stream=True)
    with open(nombreImagen, 'wb') as f:
        r.raw.decode_content = True
        shutil.copyfileobj(r.raw, f)      

    #Realizamos el conteo de palabras y lo metemos en el csv
    simbolos = ['¿','?','.','.',';',':','¡','!']
    for simbolo in simbolos:
      frase = frase.replace(simbolo,' ')
    palabras_frase = ((frase.lower()).title()).split()
    #print(palabras_frase)
    for palabra in palabras_frase:
      palabras[palabra] = palabras.get(palabra , 0) + 1 
      
    for key in palabras:
      if palabras[key] == 1:
        veces = 'vez'
      else:
        veces='veces'
      
      #print(f'La palabra {key} se ha repetido {palabras[key]} {veces}')
    
    with open('LisaSimpson/contador.csv', 'w', newline='') as file:
      fieldnames=['Palabras','N de repeticiones']
      writer=csv.DictWriter(file,fieldnames=fieldnames)
      if file.tell() == 0:
        writer.writeheader()
      for key in palabras:
        writer.writerow({'Palabras':key,'N de repeticiones':palabras[key]}) 

    #Generamos un csv con las frases de cada personaje en su carpeta
    data={"quote":frase,"character":personaje}
    nombre_csv = "LisaSimpson/" + personaje +"/"+personaje+".csv"
    with open(nombre_csv, 'a', newline='') as f:
      a=csv.DictWriter(f,data.keys())
      a.writerow(data) 
    
timer()