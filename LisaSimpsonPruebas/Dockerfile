FROM python

RUN mkdir LisaSimpson
COPY main.py ./LisaSimpson/
COPY requeriments.txt ./LisaSimpson/

RUN mkdir LisaSimpson/Homer
RUN mkdir LisaSimpson/Lisa
RUN mkdir LisaSimpson/General

RUN pip install -r ./LisaSimpson/requeriments.txt

CMD ["python","LisaSimpson/main.py"]