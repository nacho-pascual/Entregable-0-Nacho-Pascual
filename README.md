<p align="center">
<img src= "https://pics.filmaffinity.com/the_simpsons-397676780-large.jpg" width="200">
</p>

# Entregable-0-Nacho-Pascual 

El ejercico propuesto , consiste en extraer información de la api de los Simpsons para efectuar diferentes acciones propuestas. Este se encuentra dividido en 3 niveles de dificultad: Maggie,Lisa y Bart. La imagen que he elegido al principio , representa la evolución del ejercicio.

## Nivel Maggie

El nivel Maggie consistia en :

* Usando google colab crear un notebook que consuma la api de los simpsons y haga una consulta cada 30seg a la API.

* El código debe guardar cada quote en un csv dentro de una carpeta con el nombre del personaje (Lisa y Homer) y en un fichero que llamaremos general (Todos).

* Generar un fichero Docker que copie el código dentro del contenedor y se ejecute de manera autónoma. El Docker debe tener el código en una carpeta app

* El fichero docker debe crear al menos las carpetas Lisa y Homer e inicialmente solo coger citas de ellos dos.
 
<p align="center">
<img src="https://www.clipartmax.com/png/small/59-596968_about-simpsons-lisa-and-maggie-png.png" alt="About - Simpsons Lisa And Maggie Png @clipartmax.com" width="150">
 </p>

### **Contenido del Ejercicio**:
1. [DockerFile]: reune los datos con los que vamos a construir el contenedor docker .
2. [Carpeta General]: contiene las frases de todos los personajes.
3. [Carpeta Lisa]: contiene las frases de Lisa.
4. [Carpeta Homer]: contiene las frases de Homer.
5. [Main.py]: contiene el script de Python que ejecuta el código.
6. [Requerimientos.txt]: contiene las librerias que le faltan al contenedor para ejecutar el código del script de pyhon.

### **Pasos para comprobrar la correcta ejecución del contenedor:**

  1.Construir nuestra imagen:
    ```
    docker build .
    ```
    
  2.Poner en marcha el contenedor con la imagen creada :
    ```
    docker run -d <imagen>
    ```
    
  3.Entrar en el contenedor:
  ```
  docker exec -it <id_contenedor> bash
  ```
  
  4.Una vez dentro puedes  entrar en la carpeta correspondiente , elegir uno de los archivos csv y ejecutar el siguiente código para ver su contenido:
  ```
  more <csv>
  ```

## Nivel Lisa

El nivel Lisa consistia en :

* Mejorad el código para descargar la imagen del personaje y guardadla en la carpeta del mismo.

* El código debe mantener un diccionario de palabras y escribir en cada iteración en un fichero el conteo de palabras que lleva.

  a. The;1

  b. Great;2

* El código debe crear de manera dinámica las carpetas con nuevos personajes.

<p align="center">
<img src="https://www.clipartmax.com/png/small/12-121828_lisa-simpson-gif-animado-lisa-simpson.png" alt="Lisa Simpson - Gif Animado Lisa Simpson @clipartmax.com" width="150">
 </p>
 
 ### **Contenido del Ejercicio**:
1. [DockerFile]: reune los datos con los que vamos a construir el contenedor docker .
2. [Main.py]: contiene el script de Python que ejecuta el código.(Aquí se encuentra cada paso explicado en detalle)
3. [Requerimientos.txt]: contiene las librerias que le faltan al contenedor para ejecutar el código del script de pyhon.
 
### **Pasos para comprobrar la correcta ejecución del contenedor:**

  1.Construir nuestra imagen:
    ```
    docker build .
    ```
    
  2.Poner en marcha el contenedor con la imagen creada :
    ```
    docker run -d <imagen>
    ```
    
  3.Entrar en el contenedor:
  ```
  docker exec -it <id_contenedor> bash
  ```
  
  4.Una vez dentro puedes  entrar en la carpeta correspondiente , elegir uno de los archivos csv y ejecutar el siguiente código para ver su contenido:
  ```
  more <csv>
  ```

## Nivel Bart

El nivel Bart consistia en :

* Construid un Docker-compose con una imagen de un contenedor de Jupyter

* Dentro del Jupyter generad un notebook con una gráfica mostrando las palabras más habituales en las quotes

* Mostrar un listado de las carpetas y las fotos de los personajes en el jupyter

* Docker-compose debe ser capaz de hacer build del contenedor original

<p align="center">
<img src="https://www.clipartmax.com/png/small/34-343469_the-simpsons-clipart-bart-simpson-bart-simpson-easy-drawing.png" alt="The Simpsons Clipart Bart Simpson - Bart Simpson Easy Drawing " width="150">
 </p>

