#!/bin/sh
## Ask which container you wanna use
read -p "which container do you wanna start:" containername
## Start container based on name
docker start $containername
