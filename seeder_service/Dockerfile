FROM python:3.7-stretch
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python3.7", "-u", "seeder.py"]