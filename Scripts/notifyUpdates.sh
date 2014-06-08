#!/bin/bash
var=$(sudo apt-get --simulate dist-upgrade)
email_add="<address>"

if [[ "$var" =~ "packages will be upgraded" ]]
then
        echo "upgrade found"
        uname=$(uname -a)
        uptime=$(uptime)
        date=$(date)
        cp email_template.txt email
        echo -e "$uname \n" >> email
        echo -e "Uptime: $uptime\n\n" >> email
        echo -e "Updates found at: $date\n\n" >> email
        echo "$var" >> email
        sudo ssmtp $email_add < email
fi
