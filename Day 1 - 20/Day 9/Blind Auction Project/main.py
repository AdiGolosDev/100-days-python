import art

bids = {}
again = True

while again:
    print(("\n" * 20) + art.logo + "\n")

# for each new name, create a key list pair inside the dict
    name = input("Please enter your name: \n")
    if name not in bids:
        bids[name] = []

# bids are appended to the list corresponding to the person who placed them
    bid = int(input("Please enter your bid: \n"))
    bids[name].append(bid)

    a = input("Are there any other bids? "
                  "(type \"yes\" if there are, and anything else if there are not\n")
    if a != "yes":
        again = False

final = 0
person = ""
# checks each item in list for every key in the dictionary
for key in bids:
    for bid in bids[key]:
        if bid > final:
            final = bid
            person = key

print(f"\nCongratulations {person}! You won with your bid of ${final}\n")
