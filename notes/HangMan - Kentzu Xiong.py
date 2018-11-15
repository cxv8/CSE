import random
rounds = 6
word_bank = ("program", "lion", "business")
word = (word_bank[random.randint(0, 2)])
guess_word = input("Guess a letter ")
while rounds > 0:
    rounds -= 1
    if guess_word != word:
        print("You did not guessed it.")
if guess_word == word:
    print("You guessed it.")