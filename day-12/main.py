# Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random
import art

print(art.logo)
answer = random.randint(1, 100)
print(f"Pssst, the correct answer is {answer}")
level = input("Choose level, hard or easy: ")
attemps = 0
not_guess_right = False

if level == "hard":
    attemps = 5
else:
    attemps = 10

while attemps > 0 or not_guess_right:
    print(f"You have {attemps} attempts remaining to guess the number.")
    guess_num = int(input("Make a guess: "))
    if guess_num == answer:
        print(f"You got it! The answer was {answer}.")
        break
    elif guess_num > answer:
        print("Too high")
        print("Guess again")
        attemps -= 1
    else:
        print("Too low")
        print("Guess again")
        attemps -= 1

if attemps == 0:
    print("You've run out of guesses, you lose.")
