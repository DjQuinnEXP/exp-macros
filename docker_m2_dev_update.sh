#!/bin/sh
## Get name of current running container
containername=$(docker ps --format "{{.Names}}")
## Run commands to be dev ready
docker exec -it --user app -w /data/web/magento2 $containername /usr/local/bin/composer install;
docker exec -it --user app -w /data/web/magento2 $containername /usr/bin/php /data/web/magento2/bin/magento setup:upgrade --keep-generated;
docker exec -it --user app -w /data/web/magento2/tools $containername /usr/bin/npm run styles;
docker exec -it --user app -w /data/web/magento2 $containername /usr/bin/php /data/web/magento2/bin/magento c:f;