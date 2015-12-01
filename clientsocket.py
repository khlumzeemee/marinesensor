#!/usr/bin/env python
""" Simulate socket client """

import socket
import select
import sys
import os


def create_client_socket():

    #INET TCP socket
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #Non blocking socket
    #Need more code to handle this right now
    #clientsocket.setblocking(0)

    #Force address reuse (after kill)
    #clientsocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    #Connect takes a tuple as argument thus the double parenthesis
    clientsocket.connect(('localhost', 8080))

    #This client doesn't send anything, just receives
    while(True):
        try:
            data = clientsocket.recv(10)
            print ('Received', str(data))
        except KeyboardInterrupt:
            clientsocket.close()
            print("Socket closed")
            try:
                sys.exit(0)
            except SystemExit:
                os._exit(0)
    

def main():
        create_client_socket()
        
if __name__ == '__main__':
    main()
