#!/bin/sh
gnome-terminal --tab -e "ssh -L 6969:localhost:15672 app@127.0.0.1 -p222"