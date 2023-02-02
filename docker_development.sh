#!/bin/sh
containername=$(docker ps --format "{{.Names}}")
## OPEN NEW TAB WITH SSH TUNNER FOR XDEBUG
gnome-terminal --tab -e "xp x"
## OPEN NEW TAB IN CONTAINER WITH CACHE WATCHER
gnome-terminal --tab -e "docker exec -it --user app -w /data/web/magento2 $containername /data/web/.config/composer/vendor/mage2tv/magento-cache-clean/bin/cache-clean.js -w"
## OPEN NEW TAB IN CONTAINER
gnome-terminal --tab -e "xp l"
