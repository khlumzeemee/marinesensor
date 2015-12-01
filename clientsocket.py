#!/usr/bin/env python
""" Simulate socket client """

import socket
import select


def create_client_socket():
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #Force address reuse
    clientsocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    #Connect takes a tuple as argument thus the double parenthesis
    clientsocket.connect(('localhost', 8080))

    #This client doesn't send anything, just receives
    while(True):
        data = clientsocket.recv(10)
        print ('Received', str(data))
        
    clientsocket.close()
    

def main():
    create_client_socket()

if __name__ == '__main__':
    main()
