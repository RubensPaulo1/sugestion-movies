from rich import print
from rich.layout import Layout
from rich.panel import Panel
from bs4 import BeautifulSoup
import requests
import re
import os
import random


# importing imdb top 250
url = 'http://www.imdb.com/chart/top'
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")


# Extract just names
movies = soup.select('td.titleColumn')
crew = [a.attrs.get('title') for a in soup.select('td.titleColumn a')]
ratings = soup.select('strong')

# function


def cadastro():
    # arquivos de dados
    arquivoJavi = open("javi.txt", "a")
    arquivoNao = open("naovi.txt", "a")
    arquivoTalvez = open("talvez.txt", "a")
    jaVi = []
    talvez = []
    semInteresse = []
    tmpp = []
    temMovie = []

    while (True):
        # randon a number
        ax = random.randrange(1, 250)

        for movie in listMovies:
            aws = ''
            if (movie['place'] == str(ax)):
                tmpp = movie['place'], ' -', movie['movie_title'], '(' + \
                    movie['year'] + ') -', movie['star_cast'], ' ', movie['raring']
                temMovie = movie['movie_title']

        af = ''.join(tmpp)
        ad = str(af)

        layout = Layout()
        layout.split_column(
            Layout(Panel('Top 100 filmes IMDb')),
            Layout(name="topo", ratio=4),
            Layout(name="baixo", ratio=4),

        )
        layout['topo'].split_row(
            Layout(
                Panel(
                    'Sugestão de filme: \n' +
                    ad +
                    '\n\nDigite[1]: se já assistiu\nDigite[2]: se queser assistir depois\nDigite[3]: se não tem interesse em assistir')),
            Layout(
                Panel(
                    'Já vi:[bold green] ' +
                    str(jaVi).replace(
                        "'",
                        ' ') +
                    '[/bold green]')))
        layout['baixo'].split_row(
            Layout(
                Panel(
                    'Ver depois: [bold yellow]' +
                    str(talvez).replace(
                        "'",
                        ' '))),
            Layout(
                Panel(
                    'Não tehho interesse: [bold red]' +
                    str(semInteresse).replace(
                        "'",
                        ' '))))

        print(layout)

        afg = input(":")
        if (afg == '1'):
            jaVi.append(temMovie)
            tmpJavi = str(temMovie)
            arquivoJavi.write(str(tmpJavi + ' , '))
            # tmpJavi = ''
        if (afg == '2'):
            talvez.append(temMovie)
            tmpTalvez = str(temMovie)
            arquivoTalvez.write(str(tmpTalvez + ' , '))
        if (afg == '3'):
            semInteresse.append(temMovie)
            tmpNao = str(temMovie)
            arquivoNao.write(str(tmpNao + ' , '))
        os.system('clear')


def telaPrincipal():
    layout = Layout()
    layout.split_column(
        Layout(Panel('Tela Principal')),
        Layout(name='principal', ratio=2),
        Layout(name='two', ratio=7),
        Layout(name='one', ratio=1)


    )

    layout['two'].split_row(


    )
    layout['one'].split_row(
        Layout(Panel('Digite uma op:'))
    )

    layout['principal'].split_row(
        Layout(Panel('[1] cadastrar')),
        Layout(Panel('[2] Ver filmes salvos')),
        Layout(Panel('[3] Apagar filmes')),
        Layout(Panel('[4] Sair')),

    )
    print(layout)
    return input()


listMovies = []

for index in range(0, len(movies)):

    movie_string = movies[index].get_text()
    movie = (' '.join(movie_string.split()).replace('.', ' '))
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
opc=''
while(opc != '4'):
    opc = telaPrincipal()
    if(opc == '1'):
       cadastro()

    if(opc == '3'):
        arquivoJavi = open("javi.txt", "w")
        arquivoNao = open("naovi.txt", "w")
        arquivoTalvez = open("talvez.txt", "w")
        arquivoJavi.close()
        arquivoTalvez.close()
        arquivoNao.close()
