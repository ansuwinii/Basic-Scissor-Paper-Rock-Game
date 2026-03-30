'''
Scissor, Paper, Rock Game
'''

import random

choices = ["scissor", "paper", "rock"]

computer = random.choice(choices)

print("-------Welcome to the Scissor, Paper and Rock Game----------- ")
choose = input("Enter your choice: ").lower()

print(f"You have choosed {choose}\nComputer has choosed {computer}")

if computer == choose:
    print("It's an draw.")

else:
    if computer == "scissor" and choose == "paper":
        print("Computer Win.\nYou Lose.")

    elif computer == "scissor" and choose == "rock":
        print("You Win.\nComputer Lose.")

    elif computer == "paper" and choose == "scissor":
        print("You Win.\nComputer Lose.")

    elif computer == "paper" and choose == "rock":
        print("Computer Win.\nYou Lose.")

    elif computer == "rock" and choose == "scissor":
        print("Computer Win.\nYou Lose.")

    elif computer == "rock" and choose == "paper":
        print("You Win.\nComputer Lose.")

    else:
        print("Something went wrong..")
