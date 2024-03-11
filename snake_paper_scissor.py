import random

def get_user_choice():
    while True:
        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
        if user_choice in ['rock', 'paper', 'scissors']:
            return user_choice
        else:
            print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

user_wins = 0
computer_wins = 0

for _ in range(3):
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    
    print("You chose:", user_choice)
    print("Computer chose:", computer_choice)
    
    result = winner(user_choice, computer_choice)
    print(result)
    if result == "You win!":
        user_wins += 1
    elif result == "Computer wins!":
        computer_wins += 1

if user_wins > computer_wins:
    print("Congratulations! You won the game!")
elif user_wins < computer_wins:
    print("Sorry, you lost the game.")
else:
    print("It's a tie overall.")
