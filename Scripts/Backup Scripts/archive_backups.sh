#!/bin/sh

BACKUP_DIR=/path/to/backup/dir
ARCHIVE_DIR=/path/to/archive/dir

# Find the most recently modified file in both directories and store the date
BACKUP_MOD_DATE=$(find $BACKUP_DIR -type f -printf '%TY-%Tm-%Td %TT\n' | sort -r | head -n 1)
ARCHIVE_MOD_DATE=$(find $ARCHIVE_DIR -type f -printf '%TY-%Tm-%Td %TT\n' | sort -r | head -n 1)

# In order to compare the dates, convert them to seconds since 1970
BACKUP_MOD_SEC=$(date -d "$BACKUP_MOD_DATE" '+%s')
ARCHIVE_MOD_SEC=$(date -d "$ARCHIVE_MOD_DATE" '+%s')

# See if there are files in the backup directory that were created after the last backup
if [ "$BACKUP_MOD_SEC" -gt "$ARCHIVE_MOD_SEC" ]; then
	# If there are, make a backup archive
	echo "Do backup"
fi