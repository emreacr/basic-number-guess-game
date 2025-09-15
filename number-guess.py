import random

def number_game():
    number = random.randint(1, 100)
    attempts = 0
    max_attempts = 7
    print("A number between 1 and 100 has been generated!")

    while attempts < max_attempts:
        try:
            guess = int(input(f"{attempts+1}. guess (Remaining attempts: {max_attempts - attempts}): "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        attempts += 1

        if guess == number:
            print(f"Correct! You guessed it in {attempts} attempts!")
            break
        else:
            if guess < number:
                print("Try a higher number.")
            else:
                print("Try a lower number.")

            difference = abs(number - guess)
            if difference <= 5:
                print("Very close!")
            elif difference <= 15:
                print("Close!")
            else:
                print("Far!")
            print()

            
    else:
        print(f"Game over! The correct number was: {number}")

    while True:
        choice = input("Do you want to play again? (Y/N): ").strip().upper()
        if choice == 'Y':
            print("\n--- New Game ---\n")
            number_game()
            break
        elif choice == 'N':
            print("Game terminated.")
            break
        else:
            print("Please enter only Y or N.")

number_game()
