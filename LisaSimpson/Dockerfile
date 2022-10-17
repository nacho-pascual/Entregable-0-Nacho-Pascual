FROM python

RUN mkdir MaggieSimpson
COPY main.py ./MaggieSimpson/
COPY requeriments.txt ./MaggieSimpson/

RUN mkdir MaggieSimpson/Homer
RUN mkdir MaggieSimpson/Lisa
RUN mkdir MaggieSimpson/General

RUN pip install -r ./MaggieSimpson/requeriments.txt

CMD ["python","MaggieSimpson/main.py"]