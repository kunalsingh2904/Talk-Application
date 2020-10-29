# 170010012 -- Kunal Kumar

## Folder contains

    1. client.py  -- (UDP client file)
    2. server.py  -- (UDP server file)
    3. makefile   -- (makefile script to start chat)
    4. run.sh     -- (bash script to start chat)
    5. pic        -- (folder containing pics of Live demonstration)

## Run Programe

    We can run programe individually or using script.

    1. Using Bash Script -- Open Terminal in this folder and execute command "./run.sh". This will open two terminal, one for client and other for server. You can start chatting now. If you want to change port number or Ip address than open "run.sh" in text editor and change specified field.

    2. Using Make Script -- Open Terminal in this folder and execute command "make run". This will open two terminal, one for client and other for server. You can start chatting now. If you want to change port number or Ip address than open "makefile" in text editor and change specified field.

    3. Run individually -- Open Terminal and execute command "python3 server.py -p <port_number>", this will start server. Open another Terminal and execute command "python3 client.py -p <port_number> -s <ip_address>", thsi will start client. Now You can start chatting.

## Client python file -- Functions

File will first check system(input) arguments and set "localPort" and "localIp" variable with specified value.
This file contains two function:

    1. receiveData -- This function take argument as socket and this will keep listning for server message. if receive message, it will print the message on terminal and continue. if receive data for exit than it will terminate the client program by setting valriable "chatting_on" False.

    2. sendData -- This function take argument as socket and serveraddress. This will keep trying for input text from user and if got, it will send the text to server.  It will print the text on terminal and continue. if received text is for exit than it will terminate the client program by setting valriable "chatting_on" False.

## Server python file -- Functions

File will first check system(input) arguments and set "localPort" variable with specified value.
This file contains two function:

    1. receiveData -- This function take argument as socket and client_List and this will keep listning for server message. if receive message, it will print the message on terminal and update the client address and continue. if receive data for exit than it will terminate the server program by setting valriable "chatting_on" False.

    2. sendData -- This function take argument as socket and client_address. This will keep trying for input text from user and if got, it will send the text to client.  It will print the text on terminal and continue. if received text is for exit than it will terminate the server program by setting valriable "chatting_on" False.
