# learn how to count up and then down for round numbers

import random
players = ["Rj", "Sara", "Alliee", "Mome", "Dad", "Jesse"]
random.shuffle(players)
bids = [0, 0, 2, 1, 3, 1]
yesOrno = ["y", "y", "y", "n", "n", "y"]
roundNum = 1
score = {
    "Rj":"100",
    "Sara":"98",
    "Alliee":"10",
    "Mome":"9",
    "Dad":"5",
    "Jesse":"100"
    }
roundin = 7

##### Make it print every previous round


def scorecard():
    global roundin, roundNum
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

    for a in range((roundin*2) -1): # First half
        
    # Beginning of Reoccuring section

        # Fourth line (Round)

        for i in range(len(players)):
            print("|", end="")

            if roundNum < 10:
                print(" ", end="")

            print("Round:", str(roundNum), end="")

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
                if int(score[players[i]]) < 10: # Original
                    print(" ", end="") # original


            if len(players[i]) % 2 != 0: # if name is ODD

                if int(score[players[i]]) < 10: # Single digits
                    print("  ", end="")
                    
                if 100 > int(score[players[i]]) > 10: # Double digits
                    for a in range(2):
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

        roundNum += 1
    

scorecard()
