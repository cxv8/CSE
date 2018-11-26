import random
rounds = 6
word_list = ["lion", "tiger", "cat"]
word_word = word_list
guess_word = input("Guess a letter ")
if guess_word != word_list[0] or word_list[1] or word_list[2]:
    print("You did not guessed it.")
    rounds -= 1
if guess_word == word_list:
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