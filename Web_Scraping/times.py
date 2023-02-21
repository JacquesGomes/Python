import requests
from bs4 import BeautifulSoup

url = "https://www.nytimes.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

article = soup.find("section", class_="story-wrapper")
headline = article.h3
summary = article.p

print(headline)
print(summary)