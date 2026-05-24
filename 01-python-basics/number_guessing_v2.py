import random
 

secret_number = random.randint(1, 100)
attempts = 0

for guess in range(1, 101):
    attempts += 1
    print(f"Trying: {guess}")
    
    if guess == secret_number:
        print(f"You guessed the number in {i} attempts!")
        break
    elif guess < secret_number:
        print("Too low!")
    else:
        print("Too high!")
 

    choice = input("Do you want to play again? (y/n): ").lower()
    if choice != "y":
        print("Goodbye!")
        break