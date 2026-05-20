favorite_books = ["Lord of the Mysteries", "Death and the Penguin", "No Longer Human", "Hitchhikers Guide to the Galaxy"]
dostoevski_books = ["The Idiot", "Brothers Karamazov", "Crime and Punishment", "Notes from Underground", "White Nights"]

print(favorite_books[-1])
for book in favorite_books:
    print(book)

result = 1
for book in dostoevski_books:
    if book == "A Faint Heart":
        result = 0

if result == 1:
    dostoevski_books.append("A Faint Heart")

for book in dostoevski_books:
    print(book)