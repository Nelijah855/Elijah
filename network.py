import socket 
import sys
"""
class responsible for the client side connection

"""
class Client():
    
    def connector(self,host):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            

            sock.connect((host,3000))
            data=sock.recv(1000)
            message="connected by pari company"
            sock.sendall(str.encode(message))
        
            

        except:
            sys.exit(0)
        x=''
        def is_connected(self):
            if x=="connected":
                return True
            else:
                return False
            

            
    

"""
class responsible for the server  side connection

"""
class Server():
    s_host=""
    port=""
    
    def listener(self,host):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((host, 3000))
        sock.listen(100)
        """
        while True:
            new_soc,addr=sock.accept()
            new_soc.sendall('server [222.(123).453.1] company....'.encode('utf-8'))
            data=new_soc.recv(1024)
"""