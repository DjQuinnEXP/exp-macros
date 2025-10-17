#!/bin/sh
## get name of the folder to start the container in
source ./warden_get_env.sh
## cd to the folder
cd /home/djquinn/domains/$user_input
## start the container
/opt/warden/bin/warden env down
## cd back to the script directory
cd -