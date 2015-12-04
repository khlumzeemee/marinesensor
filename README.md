# marinesensor
Socket based sensor data reading application

##Resources
    - https://docs.python.org/3/howto/sockets.html
    - https://docs.python.org/3.1/library/socket.html
    - https://pymotw.com/2/select/

##Goal
    - connect to an asynchronous server socket, read and parse the socket data
    - fail safe mechanism (disconnection detection)
    - create a second synchronous socket server (HTTP style, use once and dispose) for specific queries
    - display the data in real-time in a user interface
