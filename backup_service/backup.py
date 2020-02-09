import pipes
import time
import datetime
import os

DB_HOST = os.environ['DB_HOST']
DB_USER = os.environ['DB_USER']
DB_PASSWORD = os.environ['DB_PASS']
DB_NAME = os.environ['DB_NAME']
BACKUP_PATH = os.environ['BACKUP_PATH']

DATETIME = time.strftime('%Y%m%d-%H%M%S')
PATH = BACKUP_PATH + '/' + DATETIME

os.makedirs(PATH, exist_ok=True)


dumpcmd = "mysqldump -h " + DB_HOST + " -u " + DB_USER + " -p" + DB_PASSWORD + " " + DB_NAME + " > " + pipes.quote(
    PATH) + "/" + DB_NAME + ".sql"
os.system(dumpcmd)
gzipcmd = "gzip " + pipes.quote(PATH) + "/" + DB_NAME + ".sql"
os.system(gzipcmd)

print("Your backup have been created in '" + PATH + "' directory"+ "' DATETIME " + DATETIME)
