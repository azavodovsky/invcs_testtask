import pipes
import time
import datetime
import os
import socket
import subprocess

DB_HOST = os.environ['DB_HOST']
DB_USER = os.environ['DB_USER']
DB_PASSWORD = os.environ['DB_PASS']
DB_NAME = os.environ['DB_NAME']
BACKUP_PATH = os.environ['BACKUP_PATH']
BACKUP_CLIENT_HOST = socket.gethostbyname('backup-client')
BACKUP_CLIENT_PORT = 2380


def backup_func():
    while True:
        DATETIME = time.strftime('%Y%m%d-%H%M%S')
        PATH = BACKUP_PATH + '/' + DATETIME

        os.makedirs(PATH, exist_ok=True)

        dumpcmd = "mysqldump -h " + DB_HOST + " -u " + DB_USER + " -p" + DB_PASSWORD + " " + DB_NAME + " > " + pipes.quote(
            PATH) + "/" + DB_NAME + ".sql"
        os.system(dumpcmd)
        gzipcmd = "gzip " + pipes.quote(PATH) + "/" + DB_NAME + ".sql"
        os.system(gzipcmd)

        print("Your backup have been created in '" + PATH + "' directory" + "' DATETIME " + DATETIME)

        checkdump = "ls -sh " + PATH + "/" + DB_NAME + ".sql.gz"
        getbackup = subprocess.Popen(checkdump, shell=True, stdout=subprocess.PIPE).stdout
        client_data = getbackup.read()

        if not client_data:
            s_f = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s_f.connect((BACKUP_CLIENT_HOST, BACKUP_CLIENT_PORT))
            print('FAILED: please check logs')
            s_f.sendall(str.encode("FAILED"))
            data = s_f.recv(1024).decode()
            print('Sent info for client:', repr(data))
            s_f.close()
        s_t = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s_t.connect((BACKUP_CLIENT_HOST, BACKUP_CLIENT_PORT))
        s_t.sendall(client_data)
        data = s_t.recv(1024).decode()
        print('SUCCESS: Sent info for client:', repr(data))
        s_t.close()
        time.sleep(5)


if __name__ == '__main__':
    backup_func()
