import guessing
import rps


def main():
    while True:
        print("\nWhich game do you want to play?")
        print("1. Guessing Game")
        print("2. Rock-Paper-Scissors")
        print("3. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            guessing.guessing_game()
        elif choice == "2":
            rps.rps_game()
        elif choice == "3":
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
            continue

        play_again = input(
            "\nDo you want to play again or switch games? (Y/N): "
        )

        if play_again.upper() != "Y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()

