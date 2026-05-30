import requests
import re
from bs4 import BeautifulSoup


def osint_tara(url, dosya):
    try:
        
        cevap = requests.get(url, timeout=10)
        cevap.raise_for_status()

        
        soup = BeautifulSoup(cevap.text, "html.parser")

        
        title = soup.title.string.strip() if soup.title and soup.title.string else "Başlık bulunamadı"

        
        linkler = []
        for link in soup.find_all("a", href=True):
            linkler.append(link["href"])

        
        emailler = re.findall(
            r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
            cevap.text
        )

        
        emailler = list(set(emailler))
        linkler = list(set(linkler))

        
        with open(dosya, "w", encoding="utf-8") as f:
            f.write(f"URL: {url}\n")
            f.write(f"Title: {title}\n\n")

            f.write("=== EMAİLLER ===\n")
            if emailler:
                for email in emailler:
                    f.write(email + "\n")
            else:
                f.write("Email bulunamadı.\n")

            f.write("\n=== LİNKLER ===\n")
            if linkler:
                for link in linkler:
                    f.write(link + "\n")
            else:
                f.write("Link bulunamadı.\n")

        print(f"Sonuçlar '{dosya}' dosyasına kaydedildi.")

    except requests.exceptions.RequestException as e:
        print(f"İstek hatası: {e}")
    except Exception as e:
        print(f"Beklenmeyen hata: {e}")

osint_tara("https://books.toscrape.com", "osint_rapor.txt")

