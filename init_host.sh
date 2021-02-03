#!/bin/bash
sudo killall -9 ivshmem-server
sudo rm -f /tmp/ivshmem_socket
sudo -b nohup ivshmem-server -Fv -m /dev/hugepages -l 1G </dev/null >/dev/null 2>&1 &
echo "Initializing..."
sleep 5
sudo chmod 777 /tmp/ivshmem_socket
