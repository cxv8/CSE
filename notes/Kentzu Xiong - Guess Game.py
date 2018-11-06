import random
number = (random.randint(0, 10))
guess_taken = 1
guess_number = int(input("Guess a number between 0 and 10. "))
if guess_number < number:
    print("Your guess is to low")
elif guess_number > number:
    print("Your guess is to high")
elif guess_number == number:
    print("You guessed it!. It took %s guesses." % guess_taken)
if guess_taken == 5:
    print("My guess was %s" % number)
while guess_taken < 4 and guess_number != number:
    guess_number = int(input("Guess a number between 0 and 10. "))
    guess_taken += 1
    if guess_number < number:
        print("Your guess is to low")
    elif guess_number > number:
        print("Your guess is to high")
    elif guess_number == number:
        print("You guessed it!. It took %s guesses." % guess_taken)
    if guess_taken == 4:
        print("My guess was %s." % number)