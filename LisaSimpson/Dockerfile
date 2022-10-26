#Utilizamos la misma estructura empleada en Maggie
FROM python

RUN mkdir LisaSimpson
COPY main.py ./LisaSimpson/
COPY requeriments.txt ./LisaSimpson/

RUN pip install -r ./LisaSimpson/requeriments.txt


CMD ["python","LisaSimpson/main.py"]