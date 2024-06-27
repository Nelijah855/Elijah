import socket
sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect(('127.0.0.1',1000))
sock.sendall('from client[123.] [info]'.encode(' utf-8'))
data=sock.recv(1024)





while True:
    print("[info...]data sent...")
    print("sent",data)