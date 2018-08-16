import requests
from bs4 import BeautifulSoup

page = requests.get('https://weather.gc.ca/city/pages/on-143_metric_e.html')
soup = BeautifulSoup(page.content, 'html.parser')

daytimeForecastList = soup.find_all('span', class_='high wxo-metric-hide')

for i in range(6):
    print(daytimeForecastList[i].contents[0])
