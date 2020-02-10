# invcs_testtask
# Run project locally:
  - Create .env file from env.dist
  - Run $docker-compose up -d
### Seeder-service
  - Insert new data into DB every 30 sec
### Backup-service
  - Create backup every 10 minutes
  - Log file path into container: /app/backup.log
  - Backup path: /app/backup
