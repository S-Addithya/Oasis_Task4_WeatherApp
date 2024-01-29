import requests
from bs4 import BeautifulSoup

city = input("Enter city name: ")

url = f"https://www.google.com/search?q=weather+{city}"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

temp = soup.find("div", attrs={"class": "BNeawe iBp4i AP7Wnd"}).text
weather = soup.find("div", attrs={"class": "BNeawe tAd8D AP7Wnd"}).text

print(f"Temperature: {temp}") 
print(f"Weather: {weather}")