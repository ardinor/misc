#!/bin/sh

update_mojibake()
{
	cd /opt/mojibake/apps/current
	git init
	echo "Pull from Github..."
	git pull
	source /opt/mojibake/bin/activate
	echo "Update translations...."
	pybabel compile -d mojibake/translations
	echo "Finished"
	exit 0
}

export -f update_mojibake

if [ `id -u` -eq 0 ]
then
	echo "Updating Mojibake..."
	su mojibake -c update_mojibake
else
	echo "To update, run this script as root"
	exit 1
fi

exit 0