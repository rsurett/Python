import bs4
import requests
from bs4 import BeautifulSoup
import time

ticker =[]
ticker_count = None
price_list = []
name = None
counter = 0

while name!="":
    name = input('Enter a ticker (enter"") to end: ')
    if name!="":
        ticker.append(name)

print(ticker)

def price_tracker():
    ticker_count=-1
    for i in ticker:
        ticker_count += 1
        url = 'https://finance.yahoo.com/quote/'+ticker[ticker_count]
        response=requests.get(url)
        soup=BeautifulSoup(response.text,"lxml")
        price = soup.find_all('div', {'class':'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text
        price = (price.replace(',', ''))
        price=float(price) # converts these to numbers
        return("${:4,.2f}".format(price))

while counter < 3:
    print(price_tracker())
    counter +=1
    time.sleep(0)

print("PROGRAM ENDED")
