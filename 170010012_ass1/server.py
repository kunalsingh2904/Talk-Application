import socket
import sys
import threading

localIP = ""  # Ip address (blank so that it can listen every address)
bufferSize = 1024   # buffersize
localPort = None    # port number

# checking command arguments
if len(sys.argv) != 3:
    print("Not valid Arguments")
    sys.exit()
# updating port number
if sys.argv[1] == "-p":
    localPort = int(sys.argv[2])
else:
    print("Required port number \nUse '-p <PORT_NO>' in command line")
    sys.exit()

# chatting start
chatting_on = True
# set to store clients address
clients = [None]

# Create a datagram socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Bind to address and ip
try:
    s.bind((localIP, localPort))
    # print("Server is Up")
except:
    raise Exception("Not able to bind to given port")

# Receive default message
data, addr = s.recvfrom(bufferSize)
clients[0] = addr       # update client address


def receiveData(sock, client_set):
    '''[function to receive data contineously from client]

    Args:
        sock ([socket.socket()]): [socket]
        client_set ([list]): [store client address]
    '''
    global chatting_on
    while chatting_on:
        try:
            # message receive
            data, addr = sock.recvfrom(bufferSize)
            # decode data
            data = data.decode()
            # update client
            client_set[0] = addr
            # printing data
            print("U1: ", data)
            # checking exit condition
            if data.lower() == "exit" or data.lower() == "quit":
                chatting_on = False
        except:
            pass


def sendData(sock, clients):
    '''[function to take input from user and send to server]

    Args:
        sock ([socket.socket()]): [socket]
        clients ([list]): [list of clients address]
    '''
    global chatting_on
    while chatting_on:
        if clients[0]:
            # taking input message
            text = input()
            # printing message
            print("U2: ", text)
            # getting address
            addr = clients[0]
            # encoding and Sending  text to client
            s.sendto(text.encode(), addr)
            # checking exit condition
            if text.lower() == "quit" or text.lower() == "exit":
                chatting_on = False


# creating thread to receive data
receiver = threading.Thread(target=receiveData, args=(s, clients))
receiver.daemon = True      # receiver will stop when programe terminate
receiver.start()

# creating thread to send data
sender = threading.Thread(target=sendData, args=(s, clients))
sender.daemon = True      # sender will stop when programe terminate
sender.start()


while chatting_on:
    # chat continue
    continue

# close socket
s.close()
# exit program
sys.exit()


# Output
# U1: Hi, How are you doing?
# U2: Hello, I am doing fine. What about you?
# U1: I am doing good.
# U2: Why did you choose ACN?
# U1: Liked CS 204 in 4th Sem, so thought of taking this elective
# U2: Ok. Will it be boring?
# U1: Yeah may be, but life as such is boring, so what to do!!
# U2: Point Macha.
# U2: I am already bored.
# U2: EXIT
