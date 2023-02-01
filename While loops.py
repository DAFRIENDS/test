secret_number = 9
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess = int(input("Take a Guess, from 1 - 10: "))
    guess_count += 1
    if guess == secret_number:
        print("You win! ")
        break
else:
    print("You had Three chances only..... ")