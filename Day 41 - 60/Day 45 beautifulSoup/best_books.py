from bs4 import BeautifulSoup
import requests
import json

response = requests.get("https://www.theguardian.com/books/ng-interactive/2026/may/12/the-100-best-novels-of-all-time")
guardian_text = response.text
soup = BeautifulSoup(guardian_text, "html.parser")
book_names = soup.select(selector=".bold.svelte-1tpye3j")

i = 100
books_ranked = {}
for book in book_names[1:]:
    books_ranked[i] = book.text
    i -= 1

with open("100_books.json", "w", encoding="utf-8") as file:
    json.dump(books_ranked, file, indent=4, sort_keys=True)
