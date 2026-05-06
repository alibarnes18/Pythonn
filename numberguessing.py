import random

guess_number = random.randint(1, 100)
attempts = 0

while True:
    try:
        guess = int(input("Enter a number: "))
        attempts += 1
    except ValueError:
        print("Please enter a valid number.")
        continue

    if guess == guess_number:
        print(f"You guessed the number in {attempts} attempts!")
        break
    elif guess < guess_number:
        print("Too Low!")
    else:
        print("Too High!")