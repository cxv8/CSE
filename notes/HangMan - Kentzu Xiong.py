import random
import string
print("Guess the word")
a = string.ascii_lowercase
print("These are the letters " + a)
rounds = 8
word_bank = ['turtle', 'pink', 'cat', 'dog', 'white', 'cyan', 'night', 'daytime', 'beach', 'lion']
word = random.choice(word_bank)
guess_word = list(word)
hidden = []
for i in range(len(guess_word)):
    hidden.append("*")
print ("".join(hidden))
guess = []
while rounds > 0 and hidden != guess_word:
    guess = input("Guess a letter ").lower()

    if guess_word != guess:
        rounds -= 1
        for g in range(len(guess_word)):
            if guess_word[g] == guess:
                hidden[g] = guess

    print("".join(hidden))
    if hidden == guess_word:
        print("you guessed it the word was " + word)

