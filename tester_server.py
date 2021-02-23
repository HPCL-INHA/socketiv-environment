# Process Arguments
import sys
if len(sys.argv) != 5:
    print("usage: " + sys.argv[0] + " [Port] [Command] [Time Duration]")
    exit(1)
port = int(sys.argv[1])
command = sys.argv[2]
time_duration = int(sys.argv[3])
print("Testing for " + sys.argv[3] + " minutes...")

# Setup Python Socket as Tester Server
import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ("127.0.0.1", port)
sock.bind(server_address)
sock.listen(1)
try:
    connection, client_address = sock.accept()
    
    # Setup Timer
    import time
    timeout = time.time() + 60 * time_duration
    while time.time() <= timeout:

        # Start Testing Binary Server
        import os
        os.system(command)

        # Send Start Message to Tester Client
        sock_msg = 0
        connection.sendall(bytes(str(sock_msg), 'utf8'))

        # Wait Return Message from Tester Client
        sock_rtn = int(str(connection.recv(256), 'utf8'))
        assert(sock_rtn == 0)

# Close Python Socket as Tester Server
finally:
    connection.close()