#!/bin/bash
sudo nohup ivshmem-server -Fv -m /dev/hugepages -l 1G </dev/null >/dev/null 2>&1 &
sleep 5
sudo chmod 777 /tmp/ivshmem_socket
