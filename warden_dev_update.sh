#!/bin/sh
## get name of the folder to start the container in
source ./warden_get_env.sh
## cd to the folder
cd /home/djquinn/domains/$user_input
## execute commands to be ready for futher development
/opt/warden/bin/warden shell -c 'composer install'
/opt/warden/bin/warden shell -c 'php bin/magento setup:upgrade --keep-generated'
/opt/warden/bin/warden shell -c 'cd tools; npm run styles; cd ..'
/opt/warden/bin/warden shell -c 'php bin/magento c:f'
## cd back to the script directory
cd -