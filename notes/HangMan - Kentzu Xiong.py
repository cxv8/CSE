import random
print("Guess the word")
rounds = 6
word_list1 = list("lion")
guess_word = input("Guess a letter ")

while rounds > 0 and guess_word != word_list1 or ("".join(word_list1)):
    guess_word = input("Guess a letter ")
    if guess_word != word_list1 or ("".join(word_list1)):
        print("You did not guessed it.")
        rounds -= 1
    if guess_word == "l":
        print("You guessed a letter correct.")
        index = word_list1.index(guess_word)
        word_list1.pop(index)
        word_list1.insert(index, "l")
    if guess_word == ("".join(word_list1)):
        print("The word was lion.")