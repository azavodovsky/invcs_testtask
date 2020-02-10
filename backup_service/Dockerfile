FROM python:3.7-stretch
COPY . /app
WORKDIR /app
RUN apt-get update && apt-get install -y cron mysql-client
RUN pip install -r requirements.txt

CMD ["python3.7", "-u", "backup.py"]
