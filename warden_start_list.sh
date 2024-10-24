#!/bin/sh
domainsfolder=/home/djquinn/domains
domainsfolderlist=$(ls $domainsfolder)
echo "$domainsfolderlist"
# Convert the list into a Zenity-friendly format (newline-separated and properly quoted)
formatted_list=$(echo "$domainsfolderlist" | while read -r line; do
  echo "\"$line\""
done)
## get name of the folder to start the container in
user_input=$(eval zenity --list --title="Domain" --column="Domains" $formatted_list)
## cd to the folder
cd $domainsfolder/$user_input
## start the container
/opt/warden/bin/warden env up
## cd back to the script directory
cd -