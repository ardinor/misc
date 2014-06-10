#!/bin/bash
# Checks for available updates and emails notification listing the updates
# Requires ssmtp to be setup
# Setup the below two email addresses appropriately
to_email="<address>"
from_email="<address>"

subject="Updates found for "

updates_found=false
error=false

# If ssmtp is not found, quit now
# Redirect errors? which ssmtp 2>&1?
if [[ ! -f $(which ssmtp) ]]; then
	echo "ssmtp not found! Exiting..."
	exit 1
fi

# Check for Debian derivatives
if [[ -f $(which apt-get) ]]; then
   apt-get update
   update_result=$(apt-get --simulate dist-upgrade) # returns 0 for none available
   update_found_str="packages will be upgraded"
	if [[ "$update_result" =~ update_found_str ]]; then
		updates_found=true
	fi
# Check for RHEL derivatives
elif [[ -f $(which yum) ]]; then
    update_result=$(yum check-update)
	# check-update returns 100 if updates are found, 0 if not available, 1 for error
 	exit_value=$?
	if [[ $exit_value -eq 100 ]]; then
		updates_found=true
	elif [[ $exit_value -eq 1 ]]; then
		error=true
	fi
# For openSUSE/Suse Enterprise, don't have one to test this
#elif [[ -f $(which zypper) ]]; then
# Arch
#elif [[ -f $(which pacman) ]]; then
fi

#apt-get update
#update_result=$(apt-get --simulate dist-upgrade)

if [[ "$updates_found" = true ]]; then
#if [[ "$update_result" =~ "packages will be upgraded" ]]; then
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
