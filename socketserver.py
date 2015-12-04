#!/usr/bin/env python
""" Simulate socket server """

import socket
import random
import time
import threading

class ServerSocketThread(threading.Thread):
    def __init__(self, client_socket):
        self.client_socket = client_socket

    def run(self):
        while True:
            msg = str(random.random())[2:12]
            self.client_socket.send(msg)

            print("Message sent: %s, waiting" % msg)
            time.sleep(random.randrange(5))
        
def create_server_socket():
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #serversocket.bind((socket.gethostname(), 8080))

    #Enable port reuse after kill
    serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    serversocket.bind(('localhost', 8080))
    serversocket.listen(5)
    
    while True:
        (clientsocket, address) = serversocket.accept()
        t = ServerSocketThread(clientsocket)
        t.run()
        

def main():
    create_server_socket()

if __name__ == '__main__':
    main()
