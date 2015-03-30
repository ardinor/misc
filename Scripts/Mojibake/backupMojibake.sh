#!/bin/bash

set -e

read -p "DB Username: " DB_USER
stty -echo
read -p "Password: " DB_PASS; echo
stty echo

ssh defestri mysqldump -u $DB_USER -p$DB_PASS mojibake category post tag tags > dump.sql
tar czvf dump.sql.gz dump.sql
