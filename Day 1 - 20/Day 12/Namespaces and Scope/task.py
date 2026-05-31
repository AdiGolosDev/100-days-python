enemies = 1

def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# local scope
def drink_potion():
    potion_strength = 2
    print(potion_strength)

drink_potion()
# doesn't work because potion_strength isn't global: print(potion_strength)

#global scope
player_health = 20

def print_health():
    print(f"Health: {player_health}") # can print because player_health is global

print(player_health)
