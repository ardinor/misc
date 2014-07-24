#!/bin/sh

BACKUP_DIR=/path/to/backup/dir/
ARCHIVE_DIR=/path/to/archive/dir/

# Find the most recently modified file in both directories and store the date
BACKUP_MOD_DATE=$(find $BACKUP_DIR -type f -printf '%TY-%Tm-%Td %TT\n' | sort -r | head -n 1)
ARCHIVE_MOD_DATE=$(find $ARCHIVE_DIR -type f -printf '%TY-%Tm-%Td %TT\n' | sort -r | head -n 1)

# In order to compare the dates, convert them to seconds since 1970
BACKUP_MOD_SEC=$(date -d "$BACKUP_MOD_DATE" '+%s')
ARCHIVE_MOD_SEC=$(date -d "$ARCHIVE_MOD_DATE" '+%s')

# See if there are files in the backup directory that were created after the last backup
if [ "$BACKUP_MOD_SEC" -gt "$ARCHIVE_MOD_SEC" ]; then
	# If there are, make a backup archive
	
	# First, we only want to keep 5 backups, if there's more than 5, delete the oldest
	ARCHIVE_COUNT=$(ls $ARCHIVE_DIR | wc -l)
	if [ "$ARCHIVE_COUNT" -gt "5" ]; then
		OLDEST_FILE=$(find $ARCHIVE_DIR -type f -printf '%TY-%Tm-%Td %TT %p\n' | sort | head -n 1)
		# Example result: 2014-07-22 12:53:53.8377380540 /dir/dir2/file3
		# Use awk to get the file path (which is the third item when split by spaces)
		OLD_FILE_PATH=$(echo "$OLDEST_FILE" | awk '{print $3}')
		# Remove the old file
		rm $OLD_FILE_PATH
	fi
	
	# Make the file name the modified date without seconds (e.g. 2014-07-22 12:53:53.tar.bz2)
	FILE_NAME=$(echo "$BACKUP_MOD_DATE" | awk -F'.' '{print $1}')
	# Create a tarball of the directory
	tar cjf "$ARCHIVE_DIR$FILE_NAME.tar.bz2" "$BACKUP_DIR"
fi
