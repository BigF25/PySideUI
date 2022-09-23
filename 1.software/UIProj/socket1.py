import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(("114.116.107.109", 8888))
    i=0
    while True:
        # i=i+1
        # j=i.byte
        # print(i)
        s.sendall(b"hello world")
        
        