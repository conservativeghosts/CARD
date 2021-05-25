import random

player1Hand = []
player2Hand = []
player3Hand = []
player4Hand = []
player5Hand = []
discPile = []

deck = ["Ace of Spades", "Ace of Hearts", "Ace of Clubs", "Ace of Diamonds",
    "King of Spades", "King of Hearts", "King of Clubs", "King of Diamonds",
    "Queen of Spades", "Queen of Hearts", "Queen of Clubs", "Queen of Diamonds",
    "Jack of Spades", "Jack of Hearts", "Jack of Clubs", "Jack of Diamonds",
    "10 of Spades", "10 of Hearts", "10 of Clubs", "10 of Diamonds",
    "9 of Spades", "9 of Hearts", "9 of Clubs", "9 of Diamonds",
    "8 of Spades", "8 of Hearts", "9 of Clubs", "9 of Diamonds",
    "7 of Spades", "7 of Hearts", "7 of Clubs", "7 of Diamonds",
    "6 of Spades", "6 of Hearts", "6 of Clubs", "6 of Diamonds",
    "5 of Spades", "5 of Hearts", "5 of Clubs", "5 of Diamonds",
    "4 of Spades", "4 of Hearts", "4 of Clubs", "4 of Diamonds",
    "3 of Spades", "3 of Hearts", "3 of Clubs", "3 of Diamonds",
    "2 of Spades", "2 of Hearts", "2 of Clubs", "2 of Diamonds"]

try:
    def dealingEngine():


        noPlayer = input("How many people are playing: 1-5  ")

        if noPlayer == "1":
            onePlayer()
        elif noPlayer == "2":
            twoPlayer()
        elif noPlayer == "3":
            threePlayer()
        elif noPlayer == "4":
            fourPlayer()
        elif noPlayer == "5":
            fivePlayer()
        else:
            print("I'm sorry, it is impossible to play with that number of players.")

    def onePlayer():
        while True:
            dealNumber1 = input("How many cards should I deal to player one?  ")

            for x in range(0, int(dealNumber1)):
                cardDealt1 = deck[random.randint(0, (len(deck)-1))]
                player1Hand.append(cardDealt1)
                deck.remove(cardDealt1)

            print("Player one's hand is: {}".format(player1Hand))
                
            discNum1 = input("How many cards would player one like to discard?  ")
                        
            for x in range(0, int(discNum1)):
                print("Player one's hand: {}".format(player1Hand))
                disc1 = input("What card would player one like to discard?  ")
                discPile.append(int(disc1)-1)
                player1Hand.pop(int(disc1)-1)

            print("Thank you")
            print("Player one's hand: {}".format(player1Hand))

            dealAgain = input("Would you like to 1)Replay or 2)End Game?  ")
            if dealAgain == "1":
                dealingEngine()
            else:
                break  

    def twoPlayer():
        while True:
            dealNumber1 = input("How many cards should I deal to player one?  ")

            for x in range(0, int(dealNumber1)):
                cardDealt1 = deck[random.randint(0, (len(deck)-1))]
                player1Hand.append(cardDealt1)
                deck.remove(cardDealt1)

            dealNumber2 = input("How many cards should I deal to player two?  ")
            
            for x in range(0, int(dealNumber2)):
                cardDealt2 = deck[random.randint(0, (len(deck)-1))]
                player2Hand.append(cardDealt2)
                deck.remove(cardDealt2)

            print("Player one's hand is: {}".format(player1Hand))
            print("Player two's hand is: {}".format(player2Hand))

            discNum1 = input("How many cards would player one like to discard?  ")
                        
            for x in range(0, int(discNum1)):
                print("Player one's hand: {}".format(player1Hand))
                disc1 = input("What card would player one like to discard?  ")
                discPile.append(int(disc1)-1)
                player1Hand.pop(int(disc1)-1)

            print("Thank you")
                

            discNum2 = input("How many cards would player two like to discard?  ")

            for x in range(0, int(discNum2)):
                print("Player two's hand: {}".format(player2Hand))
                disc2 = input("what card would player two like to discard?  ")
                discPile.append(int(disc2)-1)
                player2Hand.pop(int(disc2)-1)
                            
            print("Thank you")

            print("Player one's hand: {}".format(player1Hand))
            print("Player two's hand: {}".format(player2Hand))

            dealAgain = input("whould you like to 1)Replay or 2)End Game?  ")
            if dealAgain == "1":
                dealingEngine()
            else:
                break
            
    def threePlayer():
        while True:
            dealNumber1 = input("How many cards should I deal to player one?  ")

            for x in range(0, int(dealNumber1)):
                cardDealt1 = deck[random.randint(0, (len(deck)-1))]
                player1Hand.append(cardDealt1)
                deck.remove(cardDealt1)

            dealNumber2 = input("How many cards should I deal to player two?  ")
            
            for x in range(0, int(dealNumber2)):
                cardDealt2 = deck[random.randint(0, (len(deck)-1))]
                player2Hand.append(cardDealt2)
                deck.remove(cardDealt2)

            dealNumber3 = input("How many cards should I deal to player three?  ")

            for x in range(0, int(dealNumber3)):
                cardDealt3 = deck[random.randint(0, (len(deck)-1))]
                player3Hand.append(cardDealt3)
                deck.remove(cardDealt3)

            print("Player one's hand is: {}".format(player1Hand))
            print("Player two's hand is: {}".format(player2Hand))
            print("Player three's hand is: {}".format(player3Hand))

            discNum1 = input("How many cards would player one like to discard?  ")
                        
            for x in range(0, int(discNum1)):
                print("Player one's hand: {}".format(player1Hand))
                disc1 = input("what card would player one like to discard?  ")
                discPile.append(int(disc1)-1)
                player1Hand.pop(int(disc1)-1)

            print("Thank you")
                

            discNum2 = input("How many cards would player two like to discard?  ")

            for x in range(0, int(discNum2)):
                print("Player two's hand: {}".format(player2Hand))
                disc2 = input("what card would player two like to discard?  ")
                discPile.append(int(disc2)-1)
                player2Hand.pop(int(disc2)-1)
                            
            print("Thank you")

            discNum3 = input("How many cards would player three like to discard?  ")

            for x in range(0, int(discNum3)):
                print("Player three's hand: {}".format(player3Hand))
                disc3 = input("what card would player two like to discard?  ")
                discPile.append(int(disc3)-1)
                player3Hand.pop(int(disc3)-1)

            print("Thank you")

            print("Player one's hand: {}".format(player1Hand))
            print("Player two's hand: {}".format(player2Hand))
            print("Player three's hand: {}".format(player3Hand))

            dealAgain = input("whould you like to 1)Replay or 2)End Game?  ")
            if dealAgain == "1":
                dealingEngine()
            else:
                break

    def fourPlayer():
        while True:
            dealNumber1 = input("How many cards should I deal to player one?  ")

            for x in range(0, int(dealNumber1)):
                cardDealt1 = deck[random.randint(0, (len(deck)-1))]
                player1Hand.append(cardDealt1)
                deck.remove(cardDealt1)

            dealNumber2 = input("How many cards should I deal to player two?  ")
            
            for x in range(0, int(dealNumber2)):
                cardDealt2 = deck[random.randint(0, (len(deck)-1))]
                player2Hand.append(cardDealt2)
                deck.remove(cardDealt2)

            dealNumber3 = input("How many cards should I deal to player three?  ")

            for x in range(0, int(dealNumber3)):
                cardDealt3 = deck[random.randint(0, (len(deck)-1))]
                player3Hand.append(cardDealt3)
                deck.remove(cardDealt3)

            dealNumber4 = input("How many cards should I deal to player four?  ")

            for x in range(0, int(dealNumber4)):
                cardDealt4 = deck[random.randint(0, (len(deck)-1))]
                player4Hand.append(cardDealt4)
                deck.remove(cardDealt4)

            print("Player one's hand is: {}".format(player1Hand))
            print("Player two's hand is: {}".format(player2Hand))
            print("Player three's hand is: {}".format(player3Hand))
            print("player four's hand is: {}".format(player4Hand))

            discNum1 = input("How many cards would player one like to discard?  ")
                        
            for x in range(0, int(discNum1)):
                print("Player one's hand: {}".format(player1Hand))
                disc1 = input("What card would player one like to discard?  ")
                discPile.append(int(disc1)-1)
                player1Hand.pop(int(disc1)-1)

            print("Thank you")
                
            discNum2 = input("How many cards would player two like to discard?  ")

            for x in range(0, int(discNum2)):
                print("Player two's hand: {}".format(player2Hand))
                disc2 = input("What card would player two like to discard?  ")
                discPile.append(int(disc2)-1)
                player2Hand.pop(int(disc2)-1)
                            
            print("Thank you")

            discNum3 = input("How many cards would player three like to discard?  ")

            for x in range(0, int(discNum3)):
                print("Player three's hand: {}".format(player3Hand))
                disc3 = input("What card would player two like to discard?  ")
                discPile.append(int(disc3)-1)
                player3Hand.pop(int(disc3)-1)

            print("Thank you")

            discNum4 = input("How many cards would player four like to discard?  ")

            for x in range(0, int(discNum4)):
                print("Player four's hand: {}".format(player4Hand))
                disc4 = input("What card would player two like to discard?  ")
                discPile.append(int(disc4)-1)
                player4Hand.pop(int(disc4)-1)

            print("Player one's hand: {}".format(player1Hand))
            print("Player two's hand: {}".format(player2Hand))
            print("Player three's hand: {}".format(player3Hand))
            print("Player four's hand: {}".format(player4Hand))

            dealAgain = input("Would you like to 1)Replay or 2)End Game?  ")
            if dealAgain == "1":
                dealingEngine()
            else:
                break

    def fivePlayer():
        while True:
            dealNumber1 = input("How many cards should I deal to player one?  ")

            for x in range(0, int(dealNumber1)):
                cardDealt1 = deck[random.randint(0, (len(deck)-1))]
                player1Hand.append(cardDealt1)
                deck.remove(cardDealt1)

            dealNumber2 = input("How many cards should I deal to player two?  ")
            
            for x in range(0, int(dealNumber2)):
                cardDealt2 = deck[random.randint(0, (len(deck)-1))]
                player2Hand.append(cardDealt2)
                deck.remove(cardDealt2)

            dealNumber3 = input("How many cards should I deal to player three?  ")

            for x in range(0, int(dealNumber3)):
                cardDealt3 = deck[random.randint(0, (len(deck)-1))]
                player3Hand.append(cardDealt3)
                deck.remove(cardDealt3)

            dealNumber4 = input("How many cards should I deal to player four?  ")

            for x in range(0, int(dealNumber4)):
                cardDealt4 = deck[random.randint(0, (len(deck)-1))]
                player4Hand.append(cardDealt4)
                deck.remove(cardDealt4)

            dealNumber5 = input("How many cards should I deal to player five?  ")

            for x in range(0, int(dealNumber5)):
                cardDealt5 = deck[random.randint(0, (len(deck)-1))]
                player5Hand.append(cardDealt5)
                deck.remove(cardDealt5)

            print("Player one's hand is: {}".format(player1Hand))
            print("Player two's hand is: {}".format(player2Hand))
            print("Player three's hand is: {}".format(player3Hand))
            print("player four's hand is: {}".format(player4Hand))
            print("player five's hand is: {}".format(player5Hand))

            discNum1 = input("How many cards would player one like to discard?  ")
                        
            for x in range(0, int(discNum1)):
                print("Player one's hand: {}".format(player1Hand))
                disc1 = input("What card would player one like to discard?  ")
                discPile.append(int(disc1)-1)
                player1Hand.pop(int(disc1)-1)

            print("Thank you")
                
            discNum2 = input("How many cards would player two like to discard?  ")

            for x in range(0, int(discNum2)):
                print("Player two's hand: {}".format(player2Hand))
                disc2 = input("What card would player two like to discard?  ")
                discPile.append(int(disc2)-1)
                player2Hand.pop(int(disc2)-1)
                            
            print("Thank you")

            discNum3 = input("How many cards would player three like to discard?  ")

            for x in range(0, int(discNum3)):
                print("Player three's hand: {}".format(player3Hand))
                disc3 = input("What card would player two like to discard?  ")
                discPile.append(int(disc3)-1)
                player3Hand.pop(int(disc3)-1)

            print("Thank you")

            discNum4 = input("How many cards would player four like to discard?  ")

            for x in range(0, int(discNum4)):
                print("Player four's hand: {}".format(player4Hand))
                disc4 = input("What card would player two like to discard?  ")
                discPile.append(int(disc4)-1)
                player4Hand.pop(int(disc4)-1)

            discNum5 = input("How many cards would player five like to discard?  ")

            for x in range(0, int(discNum5)):
                print("Player four's hand: {}".format(player5Hand))
                disc5 = input("What card would player five like to discard?  ")
                discPile.append(int(disc5)-1)
                player4Hand.pop(int(disc5)-1)

            print("Player one's hand: {}".format(player1Hand))
            print("Player two's hand: {}".format(player2Hand))
            print("Player three's hand: {}".format(player3Hand))
            print("Player four's hand: {}".format(player4Hand))
            print("Player five's hand: {}".format(player5Hand))

            dealAgain = input("Would you like to 1)Replay or 2)End Game?  ")
            if dealAgain == "1":
                dealingEngine()
            else:
                break

except:
    print("An error has occurred")
                    
if __name__ == "__main__":
    dealingEngine()
#hmm yes my pain and suffering is over, for now. 
