import random

# 0
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
# 1
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

# 2
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

list = [rock, paper, scissors]

computer = random.randint(0, 2)

player = int(input("Please choose rock, paper or scissors: 1 - rock, 2 - paper, 3 - scissors")) - 1

if (player == 0 and computer == 2) or (player == 1 and computer == 0) or (player == 1 and computer == 3) or (player == 2 and computer == 1):
    print("You Win!")
elif player == computer:
    print("Draw")
else:
    print("You Lose!")


print(f"Player chose: {list[player]}\n Computer chose: {list[computer]}")