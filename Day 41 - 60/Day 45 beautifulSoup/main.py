from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")

yc_webpage = response.text
soup = BeautifulSoup(yc_webpage, "html.parser")

print(soup.title.text)

# titles = soup.select(selector=".titleline > a")
# titles = soup.find_all(name="span", class_="titleline")
titles = soup.select(selector=".titleline")
scores = soup.select(selector=".score")
s = []
for score in scores:
    s.append(score.text)


# t = {}
# for title in titles:
#     link = title.find("a")
#     t[link.text] = link.get("href")

# print(t)

l = []
i = 0
for title in titles:
    d = {}
    link = title.find("a")
    d["title"] = link.text
    d["link"] = link.get("href")
    d["upvotes"] = s[i]
    i+=1
    l.append(d)

print(l[0])

highest = l[0]
for _ in l:
    if int(_["upvotes"].split(' ')[0]) > int(highest["upvotes"].split(' ')[0]):
        highest = _

print(highest)

# data that is available publicly and not copyrighted is probably okay to scrape
# you can't commercialize copyrighted content
# can't scrape data behind authentication


# with open("website.html") as file:
#     contents = file.read()

# soup = BeautifulSoup(contents, 'html.parser')

# # print(soup.title.string)
# # print(soup.prettify())

# anchor_tags = soup.find_all(name="a")
# # print(anchor_tags)

# for tag in anchor_tags:
#     # print(tag.getText())
#     print(tag.get("href"))

# heading = soup.find(name="h1", id="name")
# print(heading.string) #heading.string = heading.getText()

# section_heading = soup.find(name="h3", class_="heading") #class_ instead of class because the latter is reserved in python

# company_url = soup.select_one(selector="p a") # select_one for one item, select for all items
# print(company_url.get("href"))

# headings = soup.select(".heading")
# print(headings)
