"""
Card Dealing Engine


Questions from previous class:
1. How do you represent each card?
2. A card displays three pieces of data...which ones do you need?  Which is the only piece of data that is IMPLIED by another piece?
3. How do you organize the deck, player "hands", and a discard "pile"?
4. How do you represent relative VALUE between cards?
5. How can you simulate shuffling?
6. How do you "deal"?

This document is going to be where we work on our Card Dealing Engine.
Below I'm going to be leaving you some instructions or asking questions in RED
"""

#The instructions and questions look like this

"""
So make sure that you pay attention as much as you can to the rules of
Python syntax in order to prevent errors.

Try to directly address each question above and if you need to,
you can put your pseudo code in multi-line comments like these
by using triple quotation marks
"""

#What library do you import to be able to make random selections?
#Put your data structure here that represents a card deck.  I'd suggest a list
#Should your player hands be lists too? Where is a good place to write those?
#Here's where your program starts.  What kind of loop should you use?
#Think about creating variables and assigning them input() values
#For example: dealNumber = input("How many cards should I deal?   ")
import random

player1Hand = []
player2Hand = []
player3Hand = []
player4Hand = []
player5Hand = []
discPile = []

deck = ["ace of spades", "ace of hearts", "ace of clubs", "ace of diamonds",
        "king of spades", "king of hearts", "king of clubs", "king of diamonds",
        "queen of spades", "queen of hearts", "queen of clubs", "queen of diamonds",
        "jack of spades", "jack of hearts", "jack of clubs", "jack of diamonds",
        "10 of spades", "10 of hearts", "10 of clubs", "10 of diamonds",
        "9 of spades", "9 of hearts", "9 of clubs", "9 of diamonds",
        "8 of spades", "8 of hearts", "9 of clubs", "9 of diamonds",
        "7 of spades", "7 of hearts", "7 of clubs", "7 of diamonds",
        "6 of spades", "6 of hearts", "6 of clubs", "6 of diamonds",
        "5 of spades", "5 of hearts", "5 of clubs", "5 of diamonds",
        "4 of spades", "4 of hearts", "4 of clubs", "4 of diamonds",
        "3 of spades", "3 of hearts", "3 of clubs", "3 of diamonds",
        "2 of spades", "2 of hearts", "2 of clubs", "2 of diamonds"]

def dealingEngine():

    noPlayer = input("How many people are playing: 1-5    ")

    if noPlayer == "1":
        onePlayer()
    elif noPlayer == "2":
        twoPlayer()
    else:
        print("there was an error")
            

def twoPlayer():
    while True:
        dealNumber1 = input("How many cards should I deal to player one? ")
        dealNumber2 = input("How many cards should I deal to player two? ")

        for x in range(0, int(dealNumber1)):
            cardDealt1 = deck[random.randint(0, (len(deck)-1))]
            player1Hand.append(cardDealt1)
            deck.remove(cardDealt1)

        for x in range(0, int(dealNumber2)):
            cardDealt2 = deck[random.randint(0, (len(deck)-1))]
            player2Hand.append(cardDealt2)
            deck.remove(cardDealt2)

            print("Player one's hand is:{}".format(player1Hand))
            print("Player two's hand is:{}".format(player2Hand))

            dealAgain = input("Would you like continue playing? Y/N ")
            if dealAgain.lower() == "n":
                break

            discNum1 = input("How many cards would player one like to discard?" )
                    
            for x in range(0, int(discNum1)):
                print("Player one's hand: {}".format(player1Hand))
                disc1 = input("what card would player one like to discard? (put 0 of the fist card, 1 for the second, and so on...) ")
                discPile.append(int(disc1))
                player1Hand.remove(int(disc1))

            print("Thank you")

            discNum2 = input("How many cards would player two like to discard?" )

            for x in range(0, int(discNum2)):
                print("Player two's hand: {}".format(player2Hand))
                disc2 = input("what card would player two like to discard? (put 0 of the fist card, 1 for the second, and so on...) ")
                discPile.append(int(disc2))
                player2Hand.pop(int(disc2))
                        
            print("Thank you")

            print("Player one's hand: {}".format(player1Hand))
            print("Player two's hand: {}".format(player2Hand))
                
if __name__ == "__main__":
    dealingEngine()
#How will you randomize the deck (like shuffling)? Do that inside your loop
#Start with a set number of cards (like two) that you deal to each "player"
#How do you represent the hands for each player?
