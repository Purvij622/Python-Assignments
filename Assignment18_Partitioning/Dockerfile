FROM python:3.12-slim

RUN apt-get update && \
    apt-get install -y default-jdk

WORKDIR /app

COPY . .

RUN pip install pyspark

CMD ["python", "app.py"]