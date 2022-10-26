#Definimos la Imagen que vamos a utilizar para nuestro contenedor
FROM python

#Construimos el directorio 

RUN mkdir MaggieSimpson

#Copiamos dentro de este el archivo de python y los requerimeintos de librerias

COPY main.py ./MaggieSimpson/
COPY requeriments.txt ./MaggieSimpson/

RUN mkdir MaggieSimpson/Homer
RUN mkdir MaggieSimpson/Lisa
RUN mkdir MaggieSimpson/General

#Instalamos los requerimeintos de librerias

RUN pip install -r ./MaggieSimpson/requeriments.txt

#Especificamos los comandos de ejecucíon del contenedor

CMD ["python","MaggieSimpson/main.py"]