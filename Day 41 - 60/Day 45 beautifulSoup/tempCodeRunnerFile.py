from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")

yc_webpage = response.text
soup = BeautifulSoup(yc_webpage, "html.parser")

print(soup.title.text)

# titles = soup.select(selector=".titleline > a")
# titles = soup.find_all(name="span", class_="titleline")
titles = soup.select(selector=".titleline")
t = {}
for title in titles:
    link = title.find("a")
    t[link.text] = link.get("href")

print(t)

l = []
for title in titles:
    d = {}
    link = title.find("a")
    d["title"] = link.text
    d["link"] = link.get("href")
    l.append(d)

print(l)
