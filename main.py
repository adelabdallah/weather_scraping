import requests
from bs4 import BeautifulSoup

page = requests.get('https://weather.gc.ca/city/pages/on-143_metric_e.html')
soup = BeautifulSoup(page.content, 'html.parser')

# secondSet = soup.find_all('section', class_='visible-xs mrgn-tp-md')
# secondSet.decompose()

daytimeForecastList = soup.find_all('span', class_='high wxo-metric-hide')


for forecast in daytimeForecastList:
        print(forecast.contents[0])
