# Dockerfile para ProductPage
FROM python:3.7.7-slim

WORKDIR /app

COPY . /app

# Instala las dependencias desde requirements.txt
RUN pip3 install -r requirements.txt

ENV GROUP_NUMBER=16
EXPOSE 9080

CMD ["python", "productpage.py", "9080"]