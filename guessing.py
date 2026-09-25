# Lab 1
# Group # 12
# Authors: Alycia Luppi, Nestor Carvallo, Anastasiia Golubtsova
# Date: 9/25/26

import random


def guessing_game():
    number = random.randint(1, 100)
    tries = 5

    print("I'm thinking of a number between 1 and 100.")

    for attempt in range(tries):
        tries_left = tries - attempt

        if tries_left == 1:
            prompt = "Guess what it is. You have 1 try: "
        else:
            prompt = f"Guess what it is. You have {tries_left} tries: "

        guess = int(input(prompt))

        if guess == number:
            print("You got it!")
            return

        if guess < number:
            message = "Nope! Too low."
        else:
            message = "Nope! Too high."

        remaining = tries_left - 1

        if remaining > 0:
            if remaining == 1:
                print(f"{message} Try again (1 try left):")
            else:
                print(f"{message} Try again ({remaining} tries left):")
        else:
            print(f"Nope! You lost. The number was {number}")


if __name__ == "__main__":
    while True:
        guessing_game()

        play_again = input("Do you want to play again? (Y/N): ")

        if play_again.upper() != "Y":
            break
