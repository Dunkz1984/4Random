import random

welcome = "Welcome to the Number Guessing Game!\n I'm thinking of a number between 1 and 100.\n You have 5 chances to guess the correct number."

def Game(number, chances):
    attempts = 0
    while attempts < chances:
        guess = int(input("Take a guess: "))

        if guess == number:
            print(f"Congratulations! You guessed the number {number} in {attempts} attempts.\n")
            return
        elif guess < number:
            print(f"Incorrect! The number is higher than {guess}.\n")
        elif guess > number:
            print(f"Incorrect! The number is lower than {guess}.\n")
        else:
            print("Invalid input! Please enter a number between 1 and 100.\n")
            return
        attempts += 1
        print(f"You have {chances - attempts} chances left.\n")
    if attempts > chances:
        print(f"Sorry! You've used all your chances. The correct number was {number}.\n")
        return


def main():
    print(welcome)
    number = random.randint(1, 100)

    while True:
        difficulty = int(input("Choose a difficulty level:\n1. Easy (10 chances)\n2. Medium (5 chances)\n3. Hard (3 chances)\n\nEnter your choice: "))

        print(f"Great! You have selected the {difficulty} difficulty level.\nLet's start the game!")

        if difficulty == 1:
            Game(number, 10)
        elif difficulty == 2:
            Game(number, 5)
        elif difficulty == 3:
            Game(number, 3)
        else:
            print("Invalid choice! Please select a valid difficulty level.")
            return
        again = input("Do you want to play again? (yes/no): ").strip().lower()
        if again != "yes":
            print("Thank you for playing! Goodbye.")
            break
    





if __name__ == "__main__":
    main() 