 #!/bin/sh

source backup_vars.sh

while MODDED_DIR=$(inotifywait -r -e modify,attrib,close_write,move,create,delete -q --format %w ${DIRS[@]}); do    
    NRPATH=$(dirname `readlink -m $i`)
	# We want a directory structure like /remote/server/var/www/ so get the base path and add it to the base remote path
    NRPATH="$RPATH$NRPATH"
	# Rsync doen't like it when you're trying to copy to a subdirectory of a directory that doesn't exist
	# First up, make the directory structure we want
    $SSH $RUSER@$RHOST -i $KEY -p $RPORT "mkdir -p $NRPATH"
	# Then Rsync away. Obviously this creates an SSH connection twice per directory, perhaps something to look at optimising.
	$RSYNC -az -e "$SSH -i $KEY -p $RPORT" "$MODDED_DIR" $RUSER@$RHOST:"$NRPATH" 2> $ERROR_LOG
done
