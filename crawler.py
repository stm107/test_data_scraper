import requests
from urllib.request import urlopen
import json
from bs4 import BeautifulSoup as bs
import json
import string
import time

# to use, cat to file, program prints output.

href = []

i=1
while i <= 500:
        cells = []
        # location of indexes, makes an index of game links
        url = "https://itch.io/games/top-rated?page=" + str(i)
        with urlopen(url) as response:
                soup = bs(response, 'html.parser')

        classes1 = soup.findAll('div', {'class': 'game_cell has_cover lazy_images'})

        for elem in classes1:
                cells.extend(elem.findAll('a', {'class': 'thumb_link game_link'}))

        for elem in cells:
                link = elem.get('href')
                href.append(link)
        # time.sleep(2)
        # print(i)
        i += 1
data = {}
k = 1
for link in href:
        # exception handling to supress failures and avoid crashes to unexpected input
        try:
                with urlopen(link) as response:
                        try:
                                soup = bs(response, 'html.parser')
                                game_title = soup.h1.string
                                body = soup.find('div', {'class': 'formatted_description user_formatted'}).text
                                link_to_image = soup.find('img', {'class': 'screenshot'})
                                image_href = link_to_image.get('src')
                                data[game_title] = {'id' : 000000 + k, 'image_link' : image_href, 'description' : body}
                                
                        except:
                                pass        
                        k += 1
                        time.sleep(1)
        except:
                time.sleep(90)

data_json = json.dumps(data, indent = 2)
print(data_json)



