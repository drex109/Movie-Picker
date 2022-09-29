import requests
from bs4 import BeautifulSoup
import random

def randomMovie():
    user_agent = {'User-agent': 'Brave/1.43.93'} #my preferred browser

    movies_list = []
    randomUrl = 'https://www.metacritic.com/browse/movies/score/metascore/year/filtered?year_selected='+ str(random.randrange(1940, 2022)) +'&sort=desc&view=detailed'
    url = randomUrl
    urlReq = requests.get(url,headers = user_agent, allow_redirects=False)
    soup = BeautifulSoup(urlReq.content, 'lxml')
    
    results = soup.find('div', class_='title_bump')
    movies = results.find_all('tr')
    for movie in movies:
        if movie.find('h3') is not None:
            movies_list.append(movie.find('h3').text)
    
    print(random.choice(movies_list))

randomMovie()