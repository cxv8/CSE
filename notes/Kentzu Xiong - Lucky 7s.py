import random
i = 15
rounds = 0
print("You have $15 and bet $1. If you win you get $4.")
print("15")
most_money = i
most_rounds = rounds

while i > 0:
    rounds += 1
    if most_money < i:
        most_money = i
        most_rounds = rounds
    dice1 = (random.randint(1, 6))
    dice2 = (random.randint(1, 6))
    if dice1 + dice2 != 7:
        i -= 1
        print("you lose")
        print(i)
    if dice1 + dice2 == 7:
        i += 4
        print("you win")
        print(i)
print("It took %d rounds to run out of money." % rounds)
print("The most money I had was %d" % most_money)
print("Round %d was the round I had the most money." % most_rounds)


