# Code by RJ Scruggs
# 11/29/17
# Notes

'''
(Done) Create a an app to score keep for you

Allow the app to save a scores from a previous game.

Allow to import a scorecard in the case the score program is shut or messed up

(Done) Create a rotation by removing an index of a list and appending it to the end,
    so you dont need to do a bunch of other crap

Allow editing of players before game begins

Allow rounds to be redone

Allow the score card to show stats like (how many time gone down, previous bids , etccc

Allow a score check function

(Done) Allow command to go down or prompt user how many rounds before hand

Fix "you cant bid section"

Create and print a FULL scoreboard that shows every round

Fix numOfrounds if function
'''

import time
import math


# Welcoming text
print("Welcome to Screw Your Neighbor Score Keeper!")
print("Enter the players names in order (clockwise).")
print("Please start with the person dealing.")
print("When finished, Enter an empty string!\n")

time.sleep(1)


# Set variables
players = []
playerNum = 0
roundNum = 1
bids = []
score = {}
done = False
roundin = 0
scoreCard = []
yesOrno = []
sumrounds = 1

# Establish how many rounds
def numOfrounds():
    global roundin
    print("\n")
    print("You can play up to round " + str(findMaxround())+ " (Recommended: 6-7 rounds)")
    roundin = int(input("How many rounds would you like to play up to? "))
    if roundin > findMaxround(): # Fix this to make it ask until the round is valid
        print("You can't play that many rounds\n")
        roundin = int(input("How many rounds would you like to play up to? "))


# Creates a rotation by moving the front player to the back of the list
def rotation():
    global players

    players.append(players[0])
    players.remove(players[0])

# 1 round; declares who's deal it is; stores everyones bid; and adds points if you got your bid
def rounds():
    global roundNum, players, bids

    bidSum = 0
    print("\n")
    print("Round " + str(roundNum))
    print("-----------------")

    print("It is " + players[0] + "'s deal!") # Declares who's deal it is and then moves the dealer to the back of the rotation.
    print("\n")
    rotation()

    for i in range(len(players) -1 ): # asks all players EXCEPT last player what they want to bid
        bid = int(input("What would " + players[i] + " like to bid? "))
        bids.append(bid)
    bidSum = sum(bids)


    if bidSum <= roundNum: # Prompts the user what they're NOT allowed to bid
        print("\n")
        print("You can't bid " + str(int(math.fabs(bidSum - roundNum))) + ".")

    if bidSum > roundNum: # Prompts the user what they're allowed to bid
        print("\n")
        print("You can bid whatever you want!")

    last = int(input("What would " + players[-1] + " like to bid? ")) # The bid of the last player in the rotation (aka the dealer)

    if bidSum + last != roundNum:
        bids.append(last)
    if bidSum + last == roundNum:
        print("\n")
        print("Sorry! You can't bid " + str(last) + ".")
        last = int(input("What would " + players[-1] + " like to bid? "))

    print("\n")
    print("There are " + str(bidSum + last) + " bids out of " + str(roundNum) + " card(s) dealt! ")


    trackScore()
    
    print("\n")
    print("Scoreboard:")

    print("-----------")
    
    for key in score.keys():
        print(key, ": ", score[key], sep="")
    print("\n")
    
##    bids.clear() 


# finds the max amount of rounds you can play based on how many players
def findMaxround():
    maxRound = int(52/len(players))

    return maxRound


# Enroll the players into the current round
def enroll():
    done = False


    while not done:
        name = input("Enter a name of a player: ")
        players.append(name)
        if name == "":
            done = True
            players.remove("")

    playerNum = len(players)

    for i in range(len(players)):
        score[(str(players[i]))] = 0


# Adds the score after each round
def trackScore():
    for i in range(len(players)):
        getBid = input("Did " + players[i] + " get what they bid? (y/n) ")
        if getBid == ("y") or getBid == ("Y") or getBid == ("Yes") or getBid == ("yes"):
            score[players[i]] = score[players[i]] + 10 + bids[i]
        yesOrno.append(getBid)

# Cycles the rounds by counting up and down and takes in what to do at the end of the round
def roundCycle(x):
    global roundin, roundNum

    firsthalf = True # Establishs the counting of the round as the first half of the game
    
    for i in range((x*2)-1):
        rounds()
        task = input("What would you like to do next?\n\nType '1' to end the round and go to the next round.\nType '2' to redo the round.\nType '3' for a score check.\n")
        if task == "1":
            if roundin == roundNum:
                firsthalf = False # When the peak round has been encountered, start counting down
            if firsthalf == True: # First half
                roundNum +=1
            if firsthalf == False: # Second Half
                roundNum -= 1
            bids.clear()
        if task == "2": # check to see if redo works on second half of game
            x += 1
            bids.clear()
        if task == "3":
            scorecard()
            bids.clear()
            if roundin == roundNum:
                firsthalf = False # When the peak round has been encountered, start counting down
            if firsthalf == True: # First half
                roundNum +=1
            if firsthalf == False: # Second Half
                roundNum -= 1
    sumrounds += 1
def scorecard():
    
    global roundin, roundNum, sumrounds
    # Top line

    for a in range(len(players)):
        print("+----------", end="")
        if len(players[a]) % 2 != 0: # Check if the name is odd or even and spaces accordingly
            print("-", end="")
        
    print("+")

    # Second line

    for i in range(len(players)):
        print("|", end="")
        if len(players[i]) % 2 != 0:
            for x in range(int((11 - (len(players[i])))/2)):
                print(" ", end="")
        else:
            for x in range(int((10 - (len(players[i])))/2)):
                print(" ", end="")
                
        print(players[i], end="") # Prints Names
        
        if len(players[i]) % 2 != 0:
            for x in range(int((11 - (len(players[i])))/2)):
                print(" ", end="")
        else:
            for x in range(int((10 - (len(players[i])))/2)):
                print(" ", end="")
    print("|")


    # Third line

    for a in range(len(players)):
        print("+==========", end="")
        if len(players[a]) % 2 != 0: # Check if the name is odd or even and spaces accordingly
            print("=", end="")
        
    print("+")

    
    scoreround = 1
    
    for a in range(sumrounds): # First half
        
    # Beginning of Reoccuring section

        # Fourth line (Round)

        for i in range(len(players)):
            print("|", end="")

            if roundNum < 10:
                print(" ", end="")

            print("Round:", str(scoreround), end="")

            for x in range(1):
                print(" ", end="")        
            if len(players[i]) % 2 != 0:
                print(" ", end="")

        print("|")

        # Fifth line (Bid)

        for i in range(len(players)):
            print("|", end="")
            
            for x in range(2):
                print(" ", end="")        
              
            print("Bid:", str(bids[i]), end="")

            for x in range(2):
                print(" ", end="")        
            if len(players[i]) % 2 != 0:
                print(" ", end="")
            
        print("|")

        # Sixth line (win?)

        for i in range(len(players)):
            print("|", end="")

            for x in range(2):
                print(" ", end="")

            print("Win:", yesOrno[i], end="")

            for x in range(2):
                print(" ", end="")        
            if len(players[i]) % 2 != 0:
                print(" ", end="")

        print("|")

        # Seventh line (score)

        for i in range(len(players)):
            print("|", end="")

            if 10 <= int(score[players[i]]) < 100 or int(score[players[i]]) <= 9:
                print(" ", end="")

            print("Score:", score[players[i]], end="") # Print score


            if len(players[i]) % 2 == 0: # If name is EVEN
                if int(score[players[i]]) < 10:
                    print(" ", end="")


            if len(players[i]) % 2 != 0: # if name is ODD

                if int(score[players[i]]) < 10: # Single digits
                    print("  ", end="")
                    
                if 100 > int(score[players[i]]) >= 10: # Double digits
                    print(" ", end="")
                        
                if int(score[players[i]]) >= 100: # Triple digits
                    print(" ", end="")
                    
                
        print("|")

        # Eighth line

        for i in range(len(players)):
            print("+----------", end="")
            if len(players[i]) % 2 != 0:
                print("-", end="")

        print("+")

        scoreround += 1
##    sumrounds += 1

# Main
enroll()
numOfrounds()
roundCycle(roundin)














