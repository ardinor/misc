#!/bin/bash
to_email="<address>"
from_email="<address>"
subject="Updates found for "

#Check for other distros?
#if [[ -f $(which apt-get) ]]
#then
#   apt-get update
#   update_result=$(apt-get --simulate dist-upgrade)
#   update_found_str="packages will be upgraded"
#   break
#elif [[ -f $(which yum) ]]
#then
#   update_result=$(yum update)
#   update_found_str=""
#   break
#elif [[ -f $(which zypper) ]]
#elif [[ -f $(which pacman) ]]
apt-get update
update_result=$(apt-get --simulate dist-upgrade)

if [[ "$update_result" =~ "packages will be upgraded" ]]
then
        hostname=$(hostname)
        uname=$(uname -a)
        uptime=$(uptime)
        date=$(date)
        subject="$subject $hostname"
        touch email
        echo -e "To:$to_email" >> email
        echo -e "From:$from_email" >> email
        echo -e "Subject:$subject \n" >> email
        echo -e "$uname \n" >> email
        echo -e "Uptime: $uptime\n\n" >> email
        echo -e "Updates found at: $date\n\n" >> email
        echo "$update_result" >> email
        ssmtp $email_add < email
        rm email
fi
