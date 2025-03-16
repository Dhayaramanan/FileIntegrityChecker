# File Integrity Checker

## Overview
This project is a **File Integrity Checker** that monitors file changes by hashing files and storing their hashes in a database. If a file is modified, the system logs the changes and sends a system notification.

## Features
- **Add files** to the integrity checker.
- **Remove files** from tracking.
- **Update hashes** when files change.
- **Check file integrity** against stored hashes.
- **Log all changes** in a log file.
- **Send system notifications** when modifications are detected.


### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/file-integrity-checker.git
cd file-integrity-checker
```

### 2. Initialize database and logging setup
- database is stored in **db/** directory
```bash
./setup.py
```

## Usage
### Add Files for Monitoring
```bash
./add.py /path/to/file1,/path/to/file2
```

### Update File Hashes
```bash
./update.py /path/to/file1,/path/to/file2
```

### Remove Files from Monitoring
```bash
./remove.py /path/to/file1,/path/to/file2
```

### Run the Integrity Checker
```bash
./checker.py
```

## Logs & Notifications
- Log files are stored in **logs/.**
- System notifications alert you when files are modified.

## Testing functions
- Test files are stored in the **test/** directory for local testing.


## Automating File Integrity Checks with Cron

To automatically run `checker.py` every 45 minutes, add the following line to your **crontab**:

```bash
*/45 * * * * /usr/bin/python3 /path/to/checker.py
```

### Steps to Add to Crontab:
1. Open the crontab editor:
   ```bash
   crontab -e
   ```
2. Add the above line at the end of the file.
3. Save and exit.

This will ensure that `checker.py` runs every **45 minutes** to verify file integrity.
