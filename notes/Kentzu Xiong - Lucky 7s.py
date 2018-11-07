import random

dice1 = (random.randint(1, 6))
dice2 = (random.randint(1, 6))
round = int(input("How many rounds do you want to play? "))
amount_of_money = 15
amount_of_money -= 1
if dice1 + dice2 == 7:
    print("You win! You get $5 back.")
    amount_of_money += 4
    print(amount_of_money)
for round > 0:
    dice1 = (random.randint(1, 6))
    dice2 = (random.randint(1, 6))
    round = int(input("How many rounds do you want to play? "))
    amount_of_money -= 1
    if dice1 + dice2 == 7:
        print("You win! You get $5 back.")
        amount_of_money += 4
        print(amount_of_money)