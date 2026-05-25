import requests
from bs4 import BeautifulSoup

url = "https://example.com"
cevap = requests.get(url)
soup = BeautifulSoup(cevap.text, "html.parser")

print(f"Title: {soup.title.text}")

for link in soup.find_all("a"):
    print(link.get("href"))