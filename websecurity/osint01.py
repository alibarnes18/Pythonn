import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com"
cevap = requests.get(url)
soup = BeautifulSoup(cevap.text, "html.parser")


print(soup.title.text)


for link in soup.find_all("a"):
    print(link.get("href"))