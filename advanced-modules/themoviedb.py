# themoviedb.org => film ve dizi arşivi
# themoviedb'nin sunduğu apiyi uygulamanızda kullanınız.
# Anahtar kelimeye göre arama
# En popüler film listesi
# Vizyondaki film listesi
import requests

r = requests


class TheMovieDb:
    def __init__(self):
        self.api_url = 'https://api.themoviedb.org/3/'
        self.api_key = 'd14d264b0a239760a044564ebe770769'

    def getPopulars(self):
        response = r.get(f"{self.api_url}movie/popular?api_key={self.api_key}&lamguage=en-US&page=1")

        return response.json()

    def searhMovie(self, keyword):
        response = r.get(f"{self.api_url}search/keyword?api_key={self.api_key}&query={keyword}&page=1")
        return response.json()


movieApi = TheMovieDb()

while True:
    print('\n')
    print(' Menü '.center(50, '*'))

    choice = input('1- Popular Movies\n2- Search Movie\n3- Exit\nWhat\'s your choice: ')

    if choice == '3':
        break
    else:
        if choice == '1':
            movies = movieApi.getPopulars()

            for movie in movies['results']:
                print(movie['title'])
        elif choice == '2':
            keyword = input('keyword: ')
            movies = movieApi.searhMovie(keyword=keyword)
            for movie in movies['results']:
                print(movie['name'])
