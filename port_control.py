import socket

def port_control(host, port):
    s = socket.socket()
    s.settimeout(1)
    conculsion = s.connect_ex((host, port))
    s.close()

    if conculsion == 0:
        return "Open"
    else:
        return "Close"

    print(port_control("scanme.nmap.org", 80))
    print(port_control("scanme.nmap.org", 9999))