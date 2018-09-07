from bs4 import BeautifulSoup
import urllib3
import csv
import requests

url = 'https://www.canada.ca/en/environment-climate-change/services/seasonal-weather-hazards/spring-summer.html#heat_and_humidity'
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

table = soup.select_one("table.table-accent table-bordered table table-responsive")

headers = [th.text.encode('utf-8') for th in table.select("tr th")]


with open("./weather_scraping/out.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    writer.writerow([[td.text.encode("utf-8") for td in row.find_all("td")] for row in table.select("tr + tr")])
