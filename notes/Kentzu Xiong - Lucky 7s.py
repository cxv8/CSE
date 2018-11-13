import random
i = 15
rounds = 0
print("You have $15 and bet $1. If you win you get $4.")
most_money = i
most_rounds = rounds
while i > 0:
    if most_money < i:
        most_money = i
    if most_rounds < rounds:
        most_rounds = rounds
    rounds += 1
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
    if i == 0:
        print("The most money I had was %s" % most_money)
        print("Round %s was the round I had the most money." % most_rounds)


