# Lab 1
# Group # 12
# Authors: Alycia Luppi, Nestor Carvallo, Anastasiia Golubtsova
# Date: 9/25/26

import random

CHOICES = {1: "rock", 2: "paper", 3: "scissors"}
WINNING_PAIRS = [(1, 3), (2, 1), (3, 2)]

def decide_winner (player, computer):
    if player == computer:
        return "tie"
    elif (player, computer) in WINNING_PAIRS:
        return "player"
    else:
        return "computer"

def get_player_choice():
    choice = input("Enter your choice: 1. rock, 2. paper, 3. scissors: ").strip()
    while choice not in ('1', '2', '3'):
        choice = input("Please enter 1, 2, or 3: ").strip()
    return int(choice)

def rps_game():
    computer = random.randint(1, 3)
    player = get_player_choice()
    print(f"You chose {CHOICES[player]}, computer chose {CHOICES[computer]}")

    result = decide_winner(player, computer)
    if result == "tie":
        print("It's a tie!")
    elif result == "player":
        print("You win!")
    else:
        print("You lose!")

if __name__ == "__main__":
    answer = input("Do you want to play? ").strip().lower()
    if answer in ('y', 'yes'):
        while True:
            rps_game()
            again = input("Do you want to play again? ").strip().lower()
            if again not in ('y', 'yes'):
                break
    print("Thank you for playing!")
