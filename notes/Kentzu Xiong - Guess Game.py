import random
number = (random.randint(0, 10))


guess_taken = 0

while guess_taken< 5:
    guess_number = int(input("Guess a number between 0 and 10. "))
    guess_taken += 1

    if guess_number < number:
        print("Your guess is to low")
    elif guess_number > number:
        print("Your guess is to high")
    elif guess_number == number:
        print("You guessed it!. It took %d guesses." % guess_taken)
    if guess_taken == 5:
        print("Sorry my guess was %s" % number)
    if guess_number == number:
        break



