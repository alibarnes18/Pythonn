import socket


s = socket.socket()
s.settimeout(1)  
sonuc = s.connect_ex(("192.168.1.1", 80))  
s.close()