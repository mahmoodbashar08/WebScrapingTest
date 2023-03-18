import requests
from bs4 import BeautifulSoup
import csv
def getLyric(query):

    url = "https://www.google.com/search?q=كلمات+أغنية+" + query
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299"}
    response = requests.get(url, headers=headers)


    soup = BeautifulSoup(response.content, "html.parser")
    lyrics = []
    divs = soup.select_one("div#main")
    first_level = divs.select("div.BNeawe")
    for i in range(len(first_level)):
        if first_level[i].find_all("div",{"class","BNeawe tAd8D AP7Wnd"}):
            hi = first_level[i].find_all("div",{"class","BNeawe tAd8D AP7Wnd"})
            final = hi[0].text
            return final
        else:
            return False

print(getLyric("take me to charge hozier"))
