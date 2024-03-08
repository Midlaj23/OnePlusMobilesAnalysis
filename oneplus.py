from urllib import request
from urllib.request import Request
from bs4 import BeautifulSoup
import json


url = 'https://www.flipkart.com/search?q=one+plus+mobile&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_2_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_1_2_na_na_ps&as-pos=1&as-type=RECENT&suggestionId=one+plus+mobile%7CMobiles&requestId=c9e95c49-b04d-4096-a10e-9a0e83741803&as-searchtext=on'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Referer": "https://www.flipkart.com/"
}

my_phones = []

for page in range(1, 6):  # Change '3' to the number of pages you want to scrape
    # Update the URL with the page parameter
    page_url = f'{url}&page={page}'
    request_site = Request(page_url, headers=headers)
    html = request.urlopen(request_site)
    soup = BeautifulSoup(html, 'html.parser')

    names = [name.text for name in soup.find_all('div', {'class': '_4rR01T'})]
    prices = [price.text for price in soup.find_all('div', {'class': '_30jeq3 _1_WHN1'})]
    camera = []
    battery = []
    display = []

    features = soup.find_all('li', {'class': 'rgWa7D'})
    for feature in features:
        text = feature.get_text().lower()
        if 'camera' in text:
            camera.append(feature.get_text())
        elif 'battery' in text:
            battery.append(feature.get_text())
        elif 'display' in text:
            display.append(feature.get_text())

    ratings = [rating.text for rating in soup.find_all('div', {'class': '_3LWZlK'})]

    for name, price, cam, bat, dis,rat in zip(names, prices, camera, battery, display,ratings):
        phone_info = {
            'Name': name,
            'Display': dis,
            'Camera': cam,
            'Battery': bat,
            'Rating':rat,
            'Price': price
        }
        my_phones.append(phone_info)
print(len(my_phones))

jsonfile = open("oneplus_mobiles.json","w")
json.dump(my_phones,jsonfile)

