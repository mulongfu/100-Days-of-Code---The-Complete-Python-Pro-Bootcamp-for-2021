import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

list_string = [rock, paper, scissors]
choice = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
)
print(f"{list_string[choice]}\n")
print("Computer chose:\n")
computer_chose = random.randint(0, 2)
print(list_string[computer_chose])

if choice == computer_chose:
    print("It's a draw.")
elif choice < computer_chose:
    if choice == 0 and computer_chose == 2:
        print("You win")
    else:
        print("You lose")
else:
    if choice == 2 and computer_chose == 0:
        print("You lose")
    else:
        print("You win")
