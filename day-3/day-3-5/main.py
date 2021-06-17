# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
name = name1.lower() + name2.lower()

count_true = 0
count_love = 0

count_true += name.count("t")
count_true += name.count("r")
count_true += name.count("u")
count_true += name.count("e")

count_love += name.count("l")
count_love += name.count("o")
count_love += name.count("v")
count_love += name.count("e")

score = int(str(count_true) + str(count_love))

if (score < 10) or (score > 90):
    print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
