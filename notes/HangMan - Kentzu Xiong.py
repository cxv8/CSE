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

while rounds > 0 and guess != guess_word:

    guess = [input("Guess the letter ")]
    print(guess)
    if guess != guess_word or guess != word:
        print("Guess again")
        rounds -= 1
    for i in guess_word:
        index = guess_word.index(i)
        hidden.pop(index)
        hidden.insert(index, i)

    print("".join(hidden))


