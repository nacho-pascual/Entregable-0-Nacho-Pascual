FROM python

RUN mkdir LisaSimpsonPruebas
COPY main.py ./LisaSimpsonPruebas/
COPY requeriments.txt ./LisaSimpsonPruebas/

RUN pip install -r ./LisaSimpsonPruebas/requeriments.txt


CMD ["python","LisaSimpsonPruebas/main.py"]