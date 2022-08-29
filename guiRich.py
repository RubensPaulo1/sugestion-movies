from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
import random

# importing imdb top 250
url = 'http://www.imdb.com/chart/top'
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# function


def sugestions(ran, list):
    for movie in list:
        aws = ''
        if (movie['place'] == str(ran)):
            print(
                movie['place'],
                '-',
                movie['movie_title'],
                '(' + movie['year'] + ') -',
                movie['star_cast'],
                movie['raring'])
            aws = input("Você já viu esse filme? S/N")
            if (aws == "S"):
                break
            else:
                print("VÁ VER!!!!!")
                return 0


# Extract
movies = soup.select('td.titleColumn')
crew = [a.attrs.get('title') for a in soup.select('td.titleColumn a')]
ratings = soup.select('strong')
listMovies = []

for index in range(0, len(movies)):

    movie_string = movies[index].get_text()
    movie = (' '.join(movie_string.split()).replace('.', ''))
    movie_title = movie[len(str(index)) + 1:-7]
    year = re.search('\\((.*?)\\)', movie_string).group(1)
    place = movie[:len(str(index)) - (len(movie))]
    convRatings = str(ratings[index]).split()[1]
    ratings2 = convRatings[7:10]
    data = {"place": place,
            "movie_title": movie_title,
            "raring": ratings2,
            "year": year,
            "star_cast": crew[index],
            }
    listMovies.append(data)

# randon a number
ax = random.randrange(1, 250)


# printing
tmpp = True
while (tmpp):
    # randon a number
    ax = random.randrange(1, 250)

    '''for movie in listMovies:
		aws = ''
		if(movie['place'] == str(ax)):
		    print(movie['place'], '-', movie['movie_title'], '('+movie['year']+') -', movie['star_cast'], movie['raring'])
		aws = input("Você já viu esse filme?")

		print(aws)
		#implementar uma estrutura para a não repetição de filmes
		if(aws=='sim'):
			break'''
    fin = sugestions(ax, listMovies)

    if (fin == 0):
        tmpp = False
