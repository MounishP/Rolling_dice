from random import randint


def roll_dice():
    dice1 = randint(0, 6)
    dice2 = randint(0, 6)
    print("{},{}".format(dice1, dice2))


def choice(choose):
    if choose == 'y':
        roll_dice()
    elif choose == 'n':
        print("Thank you for rolling the dice.")
        exit()
    else:
        print("Please enter y or no!")
        exit()


while True:
    choose = input("enter y or n: ")
    choice(choose)
