from urllib.request import urlopen
from bs4 import BeautifulSoup
from collections import OrderedDict
import pyexcel
from youtube_dl import YoutubeDL

url = "https://www.apple.com/itunes/charts/songs/"
connect = urlopen(url)

raw_data = connect.read()
page_content = raw_data.decode("utf8")
soup = BeautifulSoup(page_content, "html.parser")
section = soup.find("section", "section chart-grid")
ul = section.find("div", "section-content").find("ul")
song_list = ul.find_all("li")

songs = []
for infor in song_list:
    name = infor.h3.a.string
    author = infor.h4.a.string
    song = OrderedDict({"Song's Name": name, "Author": author})
    songs.append(song)

pyexcel.save_as(records=songs, dest_file_name="song_list.xlsx")

options = [{'default_search': 'ytsearch', 'max_downloads': 1},
           {'default_search': 'ytsearch', 'max_downloads': 1, 'format': 'bestaudio/audio'}]
for song in songs:
    a = [song["Song's Name"] + " " + song["Author"]]
    dl1 = YoutubeDL(options[0])
    dl1.download(a)
    dl2 = YoutubeDL(options[1])
    dl2.download(a)
