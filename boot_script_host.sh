#!/bin/bash
sudo ivshmem-server -Fv -m /dev/hugepages -l 1G
sudo chmod 777 /tmp/ivshmem_socket
