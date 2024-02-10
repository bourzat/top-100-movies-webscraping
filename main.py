import requests
from bs4 import BeautifulSoup

url = 'https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

title = soup.find_all(name='h3', class_='title')


def write_to_movies_file(strings):
    with open('movies.txt', 'w') as file:
        for movie in enumerate(reversed(strings)):
            print(movie[1])
            file.write(movie[1] + '\n')


movies = []
for text in title:
    txt = text.getText()
    movies.append(txt)

write_to_movies_file(movies)
