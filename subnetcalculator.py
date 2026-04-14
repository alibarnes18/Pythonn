import ipaddress

def subnet_analiz(cidr):
    try:
        ag = ipaddress.IPv4Network(cidr, strict=False)
        print(f"\n{'='*40}")
        print(f"Ağ: {ag}")
        print(f"Network: {ag.network_address}")
        print(f"Broadcast: {ag.broadcast_address}")
        print(f"Subnet Mask: {ag.netmask}")
        print(f"Host sayısı: {ag.num_addresses - 2}")

        hostlar = list(ag.hosts())

        print(f"Host sayısı: ", len(hostlar))
        print(f"Ilk host: ", hostlar[0])
        print(f"Son host: ", hostlar[-1])
    except Exception as e:
        print(f"Hata: {e}")

# Test et
aglar = ["192.168.1.0/24", "10.0.0.0/8", "172.16.0.0/16"]
for ag in aglar:
    subnet_analiz(ag)