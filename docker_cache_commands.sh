#!/bin/sh
cd /data/web/magento2;
pwd;
/data/web/.config/composer/vendor/mage2tv/magento-cache-clean/bin/cache-clean.js -w;
