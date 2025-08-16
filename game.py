import random

print("Welcome to Guess the Number Game!")

# Computer picks random number between 1 to 100
secret_number = random.randint(1, 100)

# Keeping track of attempts
attempts = 0

while True:
    try:
        guess = int(input("Guess the number between 1 and 100: "))
        attempts += 1

        if guess < secret_number:
            print("Too Low! Try again.")
        elif guess > secret_number:
            print("Too High! Try again.")
        else:
            print(f"🎉 Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
            break

    except ValueError:
        print("⚠️ Invalid input! Please enter only numbers.")
