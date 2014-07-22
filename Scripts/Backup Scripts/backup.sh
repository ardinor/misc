 #!/bin/sh

source backup_vars.sh

while MODDED_DIR=$(inotifywait -r -e modify,attrib,close_write,move,create,delete -q --format %w ${DIRS[@]}); do
    NRPATH=$(dirname `readlink -m $i`)
	# We want a directory structure like /remote/server/var/www/ so get the base path and add it to the base remote path
    NRPATH="$RPATH$NRPATH"
	# The directory structure should already exist as we created it in initial_backup.sh
	$RSYNC -az -e "$SSH -i $KEY -p $RPORT" "$MODDED_DIR" $RUSER@$RHOST:"$NRPATH" 2> $ERROR_LOG
done
