year = int(input("What's your year of birth?"))

if year > 1980 and year <= 1994: # has to actually include 1994 so that it doesn't bug out
    print("You are a millennial.") #idk if 1994 is millenial or not
elif year > 1994:
    print("You are a Gen Z.")
