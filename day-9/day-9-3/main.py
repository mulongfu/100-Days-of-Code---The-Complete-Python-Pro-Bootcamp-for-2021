from replit import clear
import art

# HINT: You can call clear() to clear the output in the console.

print(art.logo)
list_for_name_and_bid = {}

while True:
    name = input("What is your name? ")
    bid = int(input("Your bid? $"))
    list_for_name_and_bid[name] = bid
    continue_input = input("Are there any other bidders? yes or no ")
    if continue_input == "no":
        break
    clear()

winner = ""
winner_bid = 0
for k, v in list_for_name_and_bid.items():
    if v > winner_bid:
        max = v
        winner = k

print(f"The winner is {winner} with a bid of ${max}")
