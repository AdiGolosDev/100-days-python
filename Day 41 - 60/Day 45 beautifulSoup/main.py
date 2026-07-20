from bs4 import BeautifulSoup

with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, 'html.parser')

# print(soup.title.string)
# print(soup.prettify())

anchor_tags = soup.find_all(name="a")
# print(anchor_tags)

for tag in anchor_tags:
    # print(tag.getText())
    print(tag.get("href"))

heading = soup.find(name="h1", id="name")
print(heading.string) #heading.string = heading.getText()

section_heading = soup.find(name="h3", class_="heading") #class_ instead of class because the latter is reserved in python

company_url = soup.select_one(selector="p a") # select_one for one item, select for all items
print(company_url.get("href"))

headings = soup.select(".heading")
print(headings)
