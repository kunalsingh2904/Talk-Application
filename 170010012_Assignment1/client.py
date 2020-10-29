import socket
import sys
import threading

localIP = None  # Ip address of server
bufferSize = 1024   # buffersize
localPort = None    # port Number

# checking command arguments
if len(sys.argv) != 5:
    print("Not valid Arguments")
    sys.exit()
# updating port number
if sys.argv[1] == "-p":
    localPort = int(sys.argv[2])
elif sys.argv[3] == '-p':
    localPort = int(sys.argv[4])
else:
    print("Required port number \nUse '-p <PORT_NO>' in command line")
    sys.exit()
# updating ip address
if sys.argv[1] == "-s":
    localIP = sys.argv[2]
elif sys.argv[3] == '-s':
    localIP = sys.argv[4]
else:
    print("Required IP Address \nUse '-s <IP_Address>' in command line")
    sys.exit()

# chatting start
chatting_on = True
# server address and port
serverAddress = (localIP, localPort)

# Create a UDP socket at client side
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# sending default message to server
s.sendto("default_message".encode(), serverAddress)


def receiveData(sock):
    '''[Function to receive data from server]

    Args:
        sock ([Socket.socket()]): [socket]
    '''
    global chatting_on
    while chatting_on:
        try:
            # message receive
            data, addr = sock.recvfrom(bufferSize)
            # decode data
            data = data.decode()
            # printing data
            print("U2: ", data)
            # checking exit condition
            if data.lower() == 'exit' or data.lower() == 'quit':
                chatting_on = False
        except:
            pass


def sendData(sock, serverAddress):
    '''[Function to send data to server]

    Args:
        sock ([socket.socket()]): [socket]
        serverAddress ([ip and port]): [server address]
    '''
    global chatting_on
    while chatting_on:
        # taking input message
        text = input()
        # printing message
        print("U1: ", text)
        # encoding and Sending  text to server
        sock.sendto(text.encode(), serverAddress)
        # checking exit condition
        if text.lower() == "quit" or text.lower() == "exit":
            chatting_on = False


# creating thread to receive data
receiver = threading.Thread(target=receiveData, args=(s,))
receiver.daemon = True      # receiver will stop when programe terminate
receiver.start()

# creating thread to send data
sender = threading.Thread(target=sendData, args=(s, serverAddress))
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
