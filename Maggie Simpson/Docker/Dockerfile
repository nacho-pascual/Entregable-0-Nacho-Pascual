FROM python

RUN APT GET UPDATE


COPY ./main.py /app/
COPY ./requirements.txt /app/

WORKDIR /app/

RUN mkdir "Homer Simpson"
RUN mkdir "Lisa Simpson"
RUN mkdir "General"

RUN pip install -r requirements.txt


CMD ["python3", "main.py"]