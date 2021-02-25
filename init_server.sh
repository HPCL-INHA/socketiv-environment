#!/bin/bash
sudo rm -f /dev/null
sudo mknod -m 666 /dev/null c 1 3
echo "Server has been (re)initialized!"
