import threading
import socket

class Client( threading.Thread ):
    __clientSocket = None
    __address = None
    __port = None
   
    def __init__(self):
         threading.Thread.__init__(self)
         self.__address = socket.gethostname()
         self.__port = 49799
         self.__clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
         print("Creating client thread to deal with client!")
        
    def start(self):
        address = input("Enter IP host of server: ")
        port = int(input("Enter the port number on the server: "))
        self.__clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__clientSocket.connect((self.__address, self.__port ))
        

    def getIPAddress(self):
        return socket.gethostbyname(socket.gethostname())

    def run(self):
        try:
            while True:
                message = input("Send text: ")
                print("message from client: ", message )
                count = self.__clientSocket.recv(1024).decode()
                print("Server says: ", count)
                
        except Exception as error:
            print("Client thread caused: ", error)

            
client = Client()
client.start()
client.getIPAddress()
client.run()
