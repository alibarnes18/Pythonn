import socket

def subdomain_tara(domain, wordlist, dosya):
    
    with open(dosya, "w") as rapor:

        for sub in wordlist:
            full_domain = f"{sub}.{domain}"

            try:
                ip = socket.gethostbyname(full_domain)

                sonuc = f"[+] Bulundu: {full_domain} -> {ip}"
                print(sonuc)

                rapor.write(sonuc + "\n")

            except socket.gaierror:
                print(f"[-] Bulunamadı: {full_domain}")


subdomains = ["www", "mail", "ftp", "admin", "test", "dev", "api", "blog"]

subdomain_tara(
    domain="google.com",
    wordlist=subdomains,
    dosya="subdomain_report.txt"
)

