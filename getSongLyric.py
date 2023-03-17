#this script will take the song lyric 
import requests
from bs4 import BeautifulSoup
import csv
def songlyric(artist,song):
    songName = song.replace(" ","-")
    artistName = artist[0].upper() + artist[1:]
    print(f"https://genius.com/{artistName}-{songName}-lyrics")
    result = requests.get(f"https://genius.com/{artistName}-{songName}-lyrics")
    soup = BeautifulSoup(result.text,"html.parser")
    main = soup.find("main",{"class","SongPage__Container-sc-19xhmoi-0 buKnHw"})
    if not main:
        print("sorry it look like you didnt write the song correct")
        return 
    songInfo = main.find("div",{"class","SongPage__Section-sc-19xhmoi-3 cXvCRB"})
    songlyrics = songInfo.find("div",{"class","Lyrics__Container-sc-1ynbvzw-6 YYrds"}).text.strip()
    return songlyrics

print(songlyric("hozier","take me to church"))