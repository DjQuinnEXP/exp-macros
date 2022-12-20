#!/bin/sh
## Get name of current running container
containername=$(docker ps --format "{{.Names}}")
echo "do you wanna stop $containername"
read -n1 -p "[y,n]" input
## If input is true, disable container
case $input in
  y|Y) docker stop $containername ;;
  n|N) echo Nothing executed ;;
  *) echo Press y or n ;;
esac
