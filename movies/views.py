import requests
from bs4 import BeautifulSoup

from django.shortcuts import render


def home(request):
    url = "https://www.imdb.com/chart/moviemeter/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    table = soup.find('table',  {'class': 'chart full-width'})
    rows = table.find_all('tr')
    movies = []
    for row in rows:
        image = row.find('img')
        if image:
            movies.append(image['alt'])
    return render(request, "movies/home.html", {'movies': movies})
