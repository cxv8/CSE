import random
import string
print("Guess the word")
string.ascii_lowercase
rounds = 8
word_bank = ['turtle']
word = random.choice(word_bank)
guess_word = list(word)
hidden = []
for i in guess_word:
    hidden.append("*")
print ("".join(hidden))
guess = []
while rounds >= 0 and guess != guess_word or guess != word:
    guess.append(input("Guess a letter "))
    for guess in guess_word:
        index = guess_word.index(guess)
        guess_word.pop(index)
        guess_word.insert(index, guess)

    print("".join(guess_word))


