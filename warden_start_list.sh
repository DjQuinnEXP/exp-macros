#!/bin/sh
domainsfolder=/home/djquinn/domains
source ./warden_get_env.sh
## cd to the folder
cd $domainsfolder/$user_input
## start the container
/opt/warden/bin/warden env up
## cd back to the script directory
cd -