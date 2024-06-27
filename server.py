import socket
sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1',1000))
sock.listen(1)
while True:
    s,ad=sock.accept()
    print("listening.......")
    data=s.recv(1024).decode('utf-8')
    print(data,"data recived .....")
    s.sendall('[info] from server 192.'.encode('utf-8'))
    s.close()
    print("[client]connected") 


