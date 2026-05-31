print(type("12345"))

print(type(float(1234)))

print(type(int(1.234)))

a = int(1.634)
#python also rounds down when converting to int
print(a)

#value error
#b = int("1.342")
#print(b)

b = int(float("1.342"))
print(b)

print("Number of letters in your name: " + str(len(input("Enter your name"))))