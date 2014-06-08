#!/bin/bash
to_email="<address>"
from_email="<address>"
subject="Updates found for "

update_result=$(sudo apt-get --simulate dist-upgrade)

if [[ "$update_result" =~ "packages will be upgraded" ]]
then
        echo "upgrade found"
        hostname=$(hostname)
        uname=$(uname -a)
        uptime=$(uptime)
        date=$(date)
        subject="$subject $hostname"
        touch email
        echo -e "To:$to_email" >> test
        echo -e "From:$from_email" >> test
        echo -e "Subject:$subject \n" >> test
        echo -e "$uname \n" >> email
        echo -e "Uptime: $uptime\n\n" >> email
        echo -e "Updates found at: $date\n\n" >> email
        echo "$update_result" >> email
        ssmtp $email_add < email
        rm email
fi
