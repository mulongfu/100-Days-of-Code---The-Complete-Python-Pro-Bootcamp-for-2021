import art
import game_data
import random
from replit import clear

user_score = 0
not_end = True
random_a = game_data.data[random.randint(0, len(game_data.data) - 1)]
random_b = game_data.data[random.randint(0, len(game_data.data) - 1)]

while not_end:
    clear()
    print(art.logo)

    if user_score > 0:
        print(f"You're right! Current score: {user_score}.")

    print(
        f"Compare A: {random_a['name']}, {random_a['description']}, from {random_a['country']}."
    )
    print(art.vs)
    print(
        f"Against B: {random_b['name']}, {random_b['description']}, from {random_b['country']}."
    )

    user_answer = input(("Who has more followers? Type 'A' or 'B': ")).lower()
    if user_answer == "a":
        if random_a["follower_count"] > random_b["follower_count"]:
            user_score += 1
            random_a = random_b
            random_b = game_data.data[random.randint(0, len(game_data.data) - 1)]

        else:
            not_end = False

    else:
        if random_b["follower_count"] > random_a["follower_count"]:
            user_score += 1
            random_a = random_b
            random_b = game_data.data[random.randint(0, len(game_data.data) - 1)]

        else:
            not_end = False

if not not_end:
    clear()
    print(art.logo)
    print(f"Sorry, that's wrong. Final score: {user_score}")
