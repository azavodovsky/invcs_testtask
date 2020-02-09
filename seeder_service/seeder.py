import sys
import mysql.connector as mysql
import time
import datetime
import os

DB_HOST = os.environ['DB_HOST']
DB_USER = os.environ['DB_USER']
DB_PASS = os.environ['DB_PASS']
DB_NAME = os.environ['DB_NAME']


def service_func():
    global conn
    # waiting for database
    timeout_waiting = 45
    timeout_start = time.time()
    while time.time() < timeout_start + timeout_waiting:
        try:
            conn = mysql.connect(
                host='{}'.format(DB_HOST),
                database='{}'.format(DB_NAME),
                user='{}'.format(DB_USER),
                password='{}'.format(DB_PASS))
            break
        except mysql.errors.InterfaceError:
            print("Waiting for database...")
            time.sleep(3)
            continue
    try:
        cursor = conn.cursor()
        createtb = "CREATE TABLE ticks (id INT unsigned primary KEY AUTO_INCREMENT, created_at TIMESTAMP);"
        cursor.execute(createtb)
        cursor.close()
    except mysql.Error as err:
        print("Error with creating table: {}".format(err))
        pass
    while True:
        cursor = conn.cursor()
        ts = time.time()
        timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        qe = "INSERT INTO ticks(created_at) VALUES('{}');".format(timestamp)
        print("New data added to Database {}".format(timestamp))
        cursor.execute(qe)
        conn.commit()
        time.sleep(10)


if __name__ == '__main__':
    service_func()
