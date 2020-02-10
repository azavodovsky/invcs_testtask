#!/bin/bash

# Start the run once job.
echo "Backup service has been started, see status in app/backup.log"

# Setup a cron schedule

printenv >> /etc/environment
echo '*/1 * * * * /usr/local/bin/python3.7 /app/backup.py >> /app/backup.log 2>&1'> scheduler.txt

crontab -u root scheduler.txt
cron -f