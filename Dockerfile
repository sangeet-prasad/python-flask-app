FROM python:3.10

RUN mkdir /app
WORKDIR /app
ADD ./requirements.txt /app/
RUN pip install -r requirements.txt

ADD src/. /app/

EXPOSE 8080
CMD ["python", "/app/app.py"]