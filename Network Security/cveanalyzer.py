import requests

def cve_tara(keyword, dosya, limit=5):
    url = "https://services.nvd.nist.gov/rest/json/cves/2.0"

    params = {
        "keywordSearch": keyword,
        "resultsPerPage": limit
    }

    print(f"[*] {keyword} için CVE taranıyor...")

    try:
        cevap = requests.get(url, params=params, timeout=10)
        veri = cevap.json()
    except Exception as e:
        print("API hatası:", e)
        return

    toplam = veri.get("totalResults", 0)
    print(f"Toplam CVE: {toplam}\n")

    with open(dosya, "w", encoding="utf-8") as f:
        f.write(f"Keyword: {keyword}\n")
        f.write(f"Toplam CVE: {toplam}\n\n")

        for cve in veri.get("vulnerabilities", []):
            cve_id = cve["cve"]["id"]
            aciklama = cve["cve"]["descriptions"][0]["value"]

            print(f"[!] {cve_id}")
            print(aciklama[:120] + "...\n")

            f.write(f"{cve_id}\n")
            f.write(aciklama + "\n\n")



cve_tara("OpenSSH", "cve_report.txt", limit=5)