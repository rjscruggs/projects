import random
import time

done = False
leftOrRight = ["Left", "Right"]
limbs = ["Hand", "Foot"]
colors = ["Yellow", "Red", "Blue", "Green"]

def welcome():
    print("Welcome to Twister Teller! ")
    print("We will begin in 30 seconds!")
    print("\n")


    time.sleep(2)
    print("Starting in")
    for i in range(5, 0, -1):
        print(i)
        time.sleep(1)
    print("Begin!")


def nextMove():
    print(leftOrRight[random.randint(0,1)], limbs[random.randint(0,1)], colors[random.randint(0,3)])
    print("\n")
    for i in range(20, 0, -1):
        if i <= 10:
            print(i)
        time.sleep(1)
    print("Begin!")

def check():
    pass

welcome()
while not done:
    print("\n")
    # check()
    nextMove()
