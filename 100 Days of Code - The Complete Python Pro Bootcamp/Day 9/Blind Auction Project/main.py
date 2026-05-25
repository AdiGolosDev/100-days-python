import art

bids = {}
again = True

while again:
    print(("\n" * 20) + art.logo + "\n")

    name = input("Please enter your name: \n")
    if name not in bids:
        bids[name] = []

    bid = int(input("Please enter your bid: \n"))
    bids[name].append(bid)

    a = input("Are there any other bids? "
                  "(type \"yes\" if there are, and anything else if there are not\n")
    if a != "yes":
        again = False

final = 0
person = ""
for key in bids:
    for bid in bids[key]:
        if bid > final:
            final = bid
            person = key

print(f"\nCongratulations {person}! You won with your bid of ${final}\n")