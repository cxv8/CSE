import random
amount_of_money = 15
rounds = 0
print("You have $15 and bet $1. If you win you get $4 back.")
i = amount_of_money
while i in range(i > 0):
    rounds += 1
    dice1 = (random.randint(1, 6))
    dice2 = (random.randint(1, 6))
    if dice1 + dice2 != 7:
        i -= 1
    if dice1 + dice2 == 7:
        i += 4
        print("You win! You get $4 back.")
        print(i)
    if i == 0:
        print("It took this many %s to run out of money." % rounds)