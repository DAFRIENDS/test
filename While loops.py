guess = int(input("Guess: "))

while guess == 10:
    if guess < 9:
        print("Behind! ")
    elif guess > 9:
        print("Ahead! ")