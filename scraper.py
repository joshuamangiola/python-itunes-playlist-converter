from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv

playlist_url = "PLAYLIST_URL_GOES_HERE"
page = urlopen(playlist_url)
soup = BeautifulSoup(page, "html.parser")
playlist_title = soup.find("h1", class_="product-header__title").get_text()

track_list = soup.find("ul", class_="tracklist")

soup.find_all('tracklist-item__text__headline')

class playlistItem:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

playlist = []

for pi in track_list.select('li.tracklist-item'):
    title = pi.find("span", class_="tracklist-item__text__headline").get_text()[2:-1]
    artist = pi.find("a", class_="table__row__link--inline").get_text()
    playlist.append(playlistItem(title, artist))

with open('output.csv', 'w') as csvfile:
    fieldnames = ['Title', 'Artist']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for pi in playlist:
        writer.writerow({'Title': pi.title, 'Artist': pi.artist})
    
print(playlist_title)

for pi in playlist:
    print('\nTitle: ' + pi.title + '\nArtist: ' + pi.artist)
