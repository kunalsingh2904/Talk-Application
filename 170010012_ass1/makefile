# port Number 
port = "20001"
# Ip address of server
ip = "127.0.0.1"

# start chat -- Run command "make run"
run:
	xterm -title "UDP server" -e "python3 server.py -p $(port)" &
	xterm -title "UDP client" -e "python3 client.py -p $(port) -s $(ip)" &


# run individually
# 1. open terminal and execute command "python3 server.py -p <port_number>"
# 2. open another terminal and execute command "python3 client.py -p <port_number> -s <ip_address>"
