#!/bin/sh

WATCH_LIST[0]=/dir
WATCH_LIST[1]=/path/to
WATCH_LIST[2]=/file/to/watch

RSYNC=/usr/bin/rsync
SSH=/usr/bin/ssh

# SSH key
KEY=/key/location
# Remote user
RUSER=<USER>
# Remote host
RHOST=<HOST>
# Remote port
RPORT=<PORT>
# Remote base path
RPATH=/remote/server
# Log file to store rsync errors in
ERROR_LOG=/path/to/error/log