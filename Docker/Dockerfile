FROM python

RUN APT GET UPDATE
WORKDIR /app

COPY python_code/main.py /app
COPY python_code/requirements.txt /app


RUN mkdir "Homer Simpson"
RUN mkdir "Lisa Simpson"
RUN mkdir "General"

RUN pip install -r requirements.txt


CMD ["python3", "main.py"]