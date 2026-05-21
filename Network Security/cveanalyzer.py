import requests


def cve_tara(keyword, dosya, limit=5):

    url = "https://services.nvd.nist.gov/rest/json/cves/2.0"
    params = {"keywordSearch": "OpenSSH", "resultsPerPage": 3}

    cevap = requests.get(url, params=params)
    veri = cevap.json()

    print(f"Toplam CVE: {veri['totalResults']}")
    for cve in veri["vulnerabilities"]:
        cve_id = cve["cve"]["id"]
        aciklama = cve["cve"]["descriptions"][0]["value"]

        print(f"\n{cve_id}")
        print(aciklama[:100])