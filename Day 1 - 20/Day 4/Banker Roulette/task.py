import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

indeks = random.randint(0,4)

print(friends[indeks])

i = random.choice(friends)
print(i)

if friends[indeks] == i:
    print(f"{i} got picked twice")