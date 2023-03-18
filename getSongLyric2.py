import requests
from bs4 import BeautifulSoup
import csv
def songLyric(songName):
    # Send a GET request to Google
    if len(songName)>20 :
        query = songName[:20]
    else:
        query = songName
    url = "https://www.google.com/search?q=كلمات+أغنية+" + query
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299"}
    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.content, "html.parser")
    divs = soup.select_one("div#main")
    first_level = divs.select("div.BNeawe")
    hello = ''
    for i in range(len(first_level)):
        if first_level[i].find_all("div",{"class","BNeawe tAd8D AP7Wnd"}):
            hello = first_level[i].find_all("div",{"class","BNeawe tAd8D AP7Wnd"})
    text = ''
    for j in range(len(hello)):
        text = text + hello[j].text
    if text !="":
        return text
    else:
        text = 'i could not find the song'
        return text

print(songLyric("take me to church"))