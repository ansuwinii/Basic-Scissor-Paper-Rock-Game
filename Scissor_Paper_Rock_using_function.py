'''
Scissor, Paper, Rock Game using Function
'''

import random

choices = ["scissor", "paper", "rock"]

#Getting computer to choose a random
def computer_choice():
    '''Randomly selects a choice for the computer.'''
    computer = random.choice(choices)
    return computer

#getting player choice
def player_choice():
    '''Prompts the player to enter a valid choice.'''
    while True:
        choose = input("Enter your choice (scissor/ paper/ rock): ").lower().strip()

        if choose in choices:
            return choose
        print(f"Invalid choice '{choose}'. Please select from scissor/ paper/ rock")
        
def determine_winner(player, computer):
    '''Determining the winner using nested loop'''
    if player == computer:
        return "draw."
    
    if player == "rock":
        if computer == "scissor":
            return "player"
        else:
            return "computer"
        
    elif player == "scissor":
        if computer == "paper":
            return "player"
        else:
            return "computer"
        
    elif player == "paper":
        if computer == "rock":
            return "player"
        else:
            return "computer"
        
def display_result(player, computer, winner):
    '''Displays the winner/ result of the game..'''
    print(f"\nYou chose: {player}")
    print(f"Computer chose: {computer}")
    print("-"*60)

    if winner == "draw":
        print("It's a draw.")

    elif winner =="player":
        print("You Win!\nComputer Lose..")
    elif winner == "computer":
        print("Computer Win!\nYou Lose..")

def play_game():
    '''This is the main function of the game..'''
    print("="*60)
    print("Welcome to the Scissor, Paper, Rock Game")
    print("="*60)

    while True:
        player = player_choice()
        computer = computer_choice()
        winner = determine_winner(player, computer)

        display_result(player, computer, winner)
        
        #Asking the user if he/she wants to play again
        print()
        play_again = input("Do you want to play again? (yes/no): ").lower().strip()
        
        if play_again not in ("yes", "y"):
            print("\nThanks for playing! GoodBye!")
            print("Have a good day!!")
            break

#Entry Point
if __name__ == "__main__":
    play_game()