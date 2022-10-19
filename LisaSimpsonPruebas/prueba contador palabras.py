import requests
import time
import csv

palabras={}
def timer():
  while True:
    
    respuesta =requests.get('https://thesimpsonsquoteapi.glitch.me/quotes')
    frase=respuesta.json()[0]['quote']
    personaje=respuesta.json()[0]['character']
    print(frase)
    print(personaje)
    

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


    with open('LisaSimpsonPruebas/contador.csv', 'w', newline='') as file:
        fieldnames=['Palabras','N de repeticiones']
        writer=csv.DictWriter(file,fieldnames=fieldnames)
        if file.tell() == 0:
          writer.writeheader()
        for key in palabras:
          writer.writerow({'Palabras':key,'N de repeticiones':palabras[key]}) 


    time.sleep(3) 
timer()