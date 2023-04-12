#scrape country, capital, population and size
from bs4 import BeautifulSoup
import requests

htmldoc=requests.get('https://www.scrapethissite.com/pages/simple/')
soup=BeautifulSoup(htmldoc.text,'lxml')
countries=[]
stats=[]
#scraping the country info
for entry in soup.findAll('div',class_='country-info'):
    stats.append(entry.text.strip())
#scraping the country names
for category in soup.findAll('h3',class_='country-name'):
    countries.append(category.text.strip())    
print((countries))
#getting input for country name to return the country info
while True:
    a=input('Enter a country from the choices(case sensitive); ')
    if a in countries:
        num=countries.index(a)
        print(stats[num])
    else:
        print('Not a country....check your spelling')
