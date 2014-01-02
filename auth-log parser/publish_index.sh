#!/bin/bash

FILE=/var/www/defestri/httpdocs/bans/index.html
NEW_NAME=date --date="last month" +%b-%Y".html"
NEW_INDEX="/home/jordan/scripts/auth-log parser/index.html"

if [-f $FILE]; then
    echo "Existing file found, moving.."
    mv $FILE $NEW_NAME
fi

echo "Move file..."

mv "$NEW_INDEX" $FILE

echo "Set ownership and permissions..."

chown www-data:www-data $FILE
chmod 644 $FILE
