# Open Terminal in current directory and run command "./run.sh"
# This will open two terminal one for client and other for server
# port Number
port="20001"
# Ip address of server
ip="127.0.0.1"
# command to open server
xterm -title "UDP server" -e "python3 server.py -p $port" &
# command to open client
xterm -title "UDP client" -e "python3 client.py -p $port -s $ip" &
#
# run individually
# 1. open terminal and execute command "python3 server.py -p <port_number>"
# 2. open another terminal and execute command "python3 client.py -p <port_number> -s <ip_address>"
