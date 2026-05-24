import random

while True:  
    guess_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 7
    won = False

    while attempts < max_attempts:  
        try:
            guess = int(input("Enter a number: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        attempts += 1

        if guess == guess_number:
            print(f"You guessed the number in {attempts} attempts!")
            won = True
            break
        elif guess < guess_number:
            print("Too Low!")
        else:
            print("Too High!")

    
    if not won:
        print(f"You didn't guess it. The number was {guess_number}.")

    
    choice = input("Do you want to play again? (y/n): ").lower()

    if choice != "y":
        print("Goodbye!")
        break