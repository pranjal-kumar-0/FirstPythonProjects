import random

num = random.randint(1, 10)
print("You have 3 guesses. Guess a number between 1 and 10")
i = 0
while i < 3:
    i += 1
    guess = int(input(f"GUESS {i}: "))
    if guess == num:
        print("You win!")
        break
else:
    print("You lose!")
