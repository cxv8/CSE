import random
rounds = 6
word_a = 'l'
word_b = 'i'
word_c = 'o'
word_d = 'n'
guess_word = input("Guess a letter ")
if guess_word != word_a or word_b or word_c or word_d:
    print("You did not guessed it.")
    rounds -= 1
if guess_word == word_a:
    print("You guessed it.")
if guess_word == word_b:
    print("You guessed it.")
if guess_word == word_c:
    print("You guessed it.")
if guess_word == word_d:
    print("You guessed it.")
while rounds > 0 and guess_word != word_a + word_b + word_c + word_d:
    guess_word = input("Guess a letter ")
    if guess_word != word_a:
        print("You did not guessed it.")
        rounds -= 1
    if guess_word != word_b:
        print("You did not guessed it.")
        rounds -= 1
    if guess_word != word_c:
        print("You did not guessed it.")
        rounds -= 1
    if guess_word != word_d:
        print("You did not guessed it.")
        rounds -= 1
    if guess_word == word_a:
        print("You guessed it.")
    if guess_word == word_b:
        print("You guessed it.")
    if guess_word == word_c:
        print("You guessed it.")
    if guess_word == word_d:
        print("You guessed it.")
    if guess_word == word_a + word_b + word_c + word_d:
        print("The word was lion.")