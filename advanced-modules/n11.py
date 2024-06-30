import requests
from bs4 import BeautifulSoup

url = 'https://www.n11.com/bilgisayar/dizustu-bilgisayar'
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
}
r = requests

html = r.get(url, headers=headers).content
soup = BeautifulSoup(html, "html.parser")

liste = soup.findAll("li", {"class": "column"}, limit=1)

count = 1

for li in liste:
    link = li.a.get('href')
    p_name = li.a.h1.text
    images = li.find("div", {"class": "cardImage"}).get("data-images").split(",")
    price = li.find("div", {"class": "priceContainer"}).findAll("span")[-1].ins.text.strip(" TL")

    print(f"{count}. ürün ismi {p_name} fiyat: {price}")
    count += 1
