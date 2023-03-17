# show the top 250 movie

import requests
from bs4 import BeautifulSoup
import csv
result = requests.get("https://www.imdb.com/chart/top/")
soup = BeautifulSoup(result.text,"html.parser")
top_movie_session = soup.find("div",{"class","lister"})
top_movie_list_test = top_movie_session.find("tbody")
top_movie_list = top_movie_list_test.find_all("tr")
# print(top_movie_list[0])
for movie_list in top_movie_list:
    movie_info = movie_list.find("td",{"class":"titleColumn"}).text.strip().split()
    movie_raiting = movie_list.find("td",{"class":"ratingColumn"}).text.strip()
    rank = movie_info[0].replace('.', '')
    title = ' '.join(movie_info[1:-1])
    year = movie_info[-1].strip('()')
    print(f"{rank}. {title} : {year}, imdb rating : {movie_raiting}")
