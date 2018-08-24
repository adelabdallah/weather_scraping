import requests
from bs4 import BeautifulSoup
from matplotlib import pyplot
import numpy as np
import datetime

page = requests.get('https://weather.gc.ca/city/pages/on-143_metric_e.html')
soup = BeautifulSoup(page.content, 'html.parser')

daytimeForecastList = soup.find_all('span', class_='high wxo-metric-hide')

weatherData = list()

datesData = list()


def days_of_the_week(day_number):
    return {
        0: 'Monday',
        1: 'Tuesday',
        2: 'Wednesday',
        3: 'Thursday',
        4: 'Friday',
        5: 'Saturday',
        6: 'Sunday'
    }[day_number if day_number <= 6 else day_number - 7]  # <--- I feel like this was clever, don't care watchu think


for i in range(6):
    weatherData.append(int(daytimeForecastList[i].contents[0].replace("°", "")))


for i in range(6):
    currentDate = days_of_the_week(datetime.datetime.today().weekday() + i)

    datesData.append(currentDate)

y = np.array(weatherData)
x = np.array([0, 1, 2, 3, 4, 5])
pyplot.xticks(x, datesData)

pyplot.plot(x, y)
pyplot.ylabel('Temperature (degrees Celsius)')
pyplot.title('Temperature for the Coming Week in Toronto')

pyplot.show()
