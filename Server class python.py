import threading
import socket

class Server( threading.Thread ):

    __socket = None
    __port = None
    __host = None
    
    def __init__(self):
        threading.Thread.__init__(self)
        self.__host = socket.gethostname()
        self.__port = 49799
        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("Server running on host: ", self.getIPAddress())
    def getIPAddress(self):
            return socket.gethostbyname(socket.gethostname())
    def run(self):
        try:
            print("Binding to port: ", self.__port)
            self.__socket.bind((self.__host, self.__port))
                    
            while True:
                 self.__socket.listen(10)
                 clientSocket, clientAddress = self.__socket.accept()
                 print ('Got connection from', clientAddress)
                 self.__socket.send( str(len(message)).encode() )
                #self.__socket.send(b'Thank you for connecting; Hello, World')
        except Exception as error:
                print("invalid number", error)
        finally:
            try:
                self.__socket.close()
            
            except Exception as error:
                print("invalid number", error)

class ClientThread( threading.Thread ):
    __clientSocket = None
    __address =None
    __port = None

    def __init__(self):
        threading.Thread.__init__(self)
        self.__address = socket.gethostname()
        self.__port = 49799
        self.__clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    def getIPAddress(self):
            return socket.gethostbyname(socket.gethostname())

    def run(self):
        try:
            while True:
                message = self.__clientSocket.recv(1024).decode()
                self.__clientSocket.send( str(len(message)).encode())
                print("message from client: ", message )
                
        except Exception as error:
            print("Client thread caused: ", error)


            
           

server = Server()
client = ClientThread()
server.start()
#client.start()



