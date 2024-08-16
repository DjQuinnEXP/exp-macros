#!/bin/sh
## get name of the folder to start the container in
user_input=$(zenity --entry)
## cd to the folder
cd /home/djquinn/domains/$user_input
## start the container
/opt/warden/bin/warden env up
## cd back to the script directory
cd -