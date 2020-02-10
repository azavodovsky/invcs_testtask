# invcs_testtask
# Run project locally:
  - Create .env file from env.dist
  - Run $docker-compose up -d
### Seeder-service
  - Insert new data into DB every 30 sec
### Backup-service
  - Create backup every 5 seconds
  - Log file path into container: /app/backup.log
  - Backup path: /app/backup
### Backup-client
  - Receive from backup-service backup STATUS
  - Logs situated at service.log
