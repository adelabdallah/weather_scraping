import requests
from bs4 import BeautifulSoup

page = requests.get('https://weather.gc.ca/city/pages/on-143_metric_e.html')
soup = BeautifulSoup(page.content, 'html.parser')

# daytimeForecastList = soup.select('wxRow.span.wxperiod_temp.daytime')
daytimeForecastList = soup.find_all('span', class_='high wxo-metric-hide')

for forecast in daytimeForecastList:
        print(forecast.prettify())
