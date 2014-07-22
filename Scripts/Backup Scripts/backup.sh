 #!/bin/sh

source WATCH_LIST.sh

RSYNC=/usr/bin/rsync
SSH=/usr/bin/ssh

KEY=/key/location
RUSER=<USER>
RHOST=<HOST>
RPORT=<PORT>
RPATH=/remote/server
ERROR_LOG=/path/to/error/log

while MODDED_DIR=$(inotifywait -r -e modify,attrib,close_write,move,create,delete -q --format %w ${DIRS[@]}); do
    if [[ -d $MODDED_DIR ]]; then
        BASE=$(basename $MODDED_DIR)
    elif [[ -f $MODDED_DIR ]]; then
        BASE=$(basename `dirname $MODDED_DIR`)		
    fi
	$RSYNC -az -e "$SSH -i $KEY -p $RPORT" "$MODDED_DIR" $RUSER@$RHOST:"$RPATH/$BASE" 2> $ERROR_LOG
done
