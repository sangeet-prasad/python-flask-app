FROM python:alpine

### Upgrade pip
RUN pip install --upgrade pip 

### App user setup
RUN adduser -D appuser
USER appuser
WORKDIR /home/appuser

### Set appuser as owner of requierements.txt
COPY --chown=appuser:appuser requirements.txt requirements.txt

### Install flask
RUN pip install --user -r requirements.txt

### Set env for appuser
ENV PATH="/home/appuser/.local/bin:${PATH}"

### Copy src code and set permissions
COPY --chown=appuser:appuser src/. .

EXPOSE 8080

CMD ["python", "/app/app.py"]