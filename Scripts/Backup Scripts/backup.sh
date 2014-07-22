 #!/bin/sh

source WATCH_LIST.sh

while MODDED_DIR=$(inotifywait -r -e modify,attrib,close_write,move,create,delete -q --format %w ${DIRS[@]}); do
    if [[ -d $MODDED_DIR ]]; then
        BASE=$(basename $MODDED_DIR)
    elif [[ -f $MODDED_DIR ]]; then
        BASE=$(basename `dirname $MODDED_DIR`)
    fi
    echo "$BASE"
done
