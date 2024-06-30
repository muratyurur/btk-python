import requests
from bs4 import BeautifulSoup

url = 'https://www.imdb.com/chart/toptv/?ref_=nv_tvv_250'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
}

r = requests

html = r.get(url, headers=headers).content

soup = BeautifulSoup(html, 'html.parser')

liste = soup.find("ul", {"class": "ipc-metadata-list"}).findAll("li", limit=10)

for item in liste:
    film_name = item.find('h3', {'class': 'ipc-title__text'}).text
    film_rating_star = item.find('span', {'class': 'ipc-rating-star'}).text
    print(film_name, film_rating_star)
