import ipaddress

def subnet_analiz(cidr):
    try:
        ag = ipaddress.IPv4Network(cidr, strict=False)

        print(f"\n{'='*40}")
        print(f"Ağ: {ag}")
        print(f"Network: {ag.network_address}")
        print(f"Broadcast: {ag.broadcast_address}")
        print(f"Subnet Mask: {ag.netmask}")
        print("Toplam address:", ag.num_addresses)

        
        first_host = None
        last_host = None
        count = 0

        for ip in ag.hosts():
            if first_host is None:
                first_host = ip
            last_host = ip
            count += 1

        print("Host sayısı:", count)
        print("İlk host:", first_host)
        print("Son host:", last_host)

        return ag  

    except Exception as e:
        print(f"Hata: {e}")
        return None



cidr = input("CIDR gir: ")

ag = subnet_analiz(cidr)


if ag:
    with open("hosts.txt", "w") as f:
        for ip in ag.hosts():
            f.write(str(ip) + "\n")



aglar = ["192.168.1.0/24", "10.0.0.0/16", "172.16.0.0/24"]

for ag_str in aglar:
    subnet_analiz(ag_str)