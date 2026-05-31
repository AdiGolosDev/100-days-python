for number in range(0, 10): #0 is included, but 10 is not
    if number % 2 == 0:
        print(number)

#step size
for number in range(0, 11, 3):
    print(number)


sum = 0
for number in range(1, 101):
    sum += number

print(sum)