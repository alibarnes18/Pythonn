def topla(a, b):
    print(a+b)


def port_tara(ip, port=80):
    print(f"{ip}:{port} scanning...")

port_tara("192.168.1.1")
port_tara("10.0.0.1", 8080)

def tum_portları_tara(ip, *portlar):
    for port in portlar:
     print(f"{ip}:{port}")

tum_portları_tara("10.0.0.1", 80, 443, 22, 8080)



def port_açıkmı(port):
   açik_port = [80, 443, 22]
   return port in açik_port

print(port_açıkmı(80))  
print(port_açıkmı(8080)) 
