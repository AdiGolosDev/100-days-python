if 3 > 2:
    a_variable = 10 # this is still global scope

game_level = 3
enemies = ["skeleton", "Zombie", "Alien"]

def create_enemy():
    # new_enemy = ""  ## this fixes the issue below
    if game_level < 5:
        new_enemy = enemies[0]

    print(new_enemy) # in this case if game_level > 5 print(new_enemy) won't be called