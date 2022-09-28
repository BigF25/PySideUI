import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(("101.43.166.212", 1234))
    i=0
    while True:
        # i=i+1
        # j=i.byte
        # print(i)
        s.sendall(b"hello world")
        
        