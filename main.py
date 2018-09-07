import requests
from bs4 import BeautifulSoup
from matplotlib import pyplot
import numpy as np
import datetime

page = requests.get('https://weather.gc.ca/city/pages/on-143_metric_e.html')
soup = BeautifulSoup(page.content, 'html.parser')

daytimeHigh = soup.find_all('span', class_='high wxo-metric-hide')
daytimeLow = soup.find_all('span', class_='low wxo-metric-hide')

weatherHighData = list()
weatherLowData = list()

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
    }[day_number if day_number <= 6 else day_number - 7]  # <--- I'm happy with this


for i in range(6):
    weatherHighData.append(int(daytimeHigh[i].contents[0].replace("°", "")))
    weatherLowData.append(int(daytimeLow[i].contents[0].replace("°", "")))


for i in range(6):
    currentDate = days_of_the_week(datetime.datetime.today().weekday() + i + 1)

    datesData.append(currentDate)

y_high = np.array(weatherHighData)
y_low = np.array(weatherLowData)
x = np.array([0, 1, 2, 3, 4, 5])
pyplot.xticks(x, datesData)

pyplot.gca().set_color_cycle(['red', 'blue'])
pyplot.plot(x, y_high, marker='o')
pyplot.plot(x, y_low, marker='o')
pyplot.ylabel('Temperature (degrees Celsius)')
pyplot.title('Temperature for the Coming Week in Toronto')
pyplot.legend(['High', 'Low'], loc='upper center')
pyplot.grid(linestyle='dashed')


pyplot.show()
