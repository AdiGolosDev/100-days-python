import art

bids = {}
again = True

while again:
    print(("\n" * 20) + art.logo + "\n")

    name = input("Please enter your name: \n")
    bid = int(input("Please enter your bid: \n"))
    bids[name] = bid

    a = input("Are there any other bids? "
                  "(type \"yes\" if there are, and anything else if there are not\n")
    if a != "yes":
        again = False

final = 0
person = ""
for key in bids:
    if bids[key] > final:
        final = bids[key]
        person = key

print(f"\nCongratulations {person}! You won with your bid of ${final}\n")