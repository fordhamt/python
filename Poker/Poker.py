#!/user/bin/env python
from __future__ import print_function # print()
from random import shuffle

class Card:
    def __init__(self):
        self.rank = None
        self.suit = None

        suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
        ranks = ["two", "three", "four", "five", "six", "seven", "eight", "9", "10", "Jack", "Queen", "King", "Ace"]

    def setSuit(self, s):
        self.suit = s

    def setRank(self, r):
        self.rank = r

    def getRank(self):
        return self.rank
 
    def getSuit(self):
        return self.suit

    def __str__(self):
        return str(self.rank) + " of " + self.suit + ", "

class Deck:
    def __init__(self):
        self.cards = []
        for i in range(0,52):
            card = Card()
            value = (i%13) + 2
            p = str(value)
            if(i < 13):
                card.setSuit("Hearts")
            elif((i >= 13) and (i <26)):
                card.setSuit("Clubs")
            elif((i >=26) and (i < 39)):
                card.setSuit("Spades")
            elif((i >= 39) and (i < 53)):
                card.setSuit("Diamonds")

            card.setRank(value)
            self.cards.append(card)

        for i in range(0,10):
            shuffle(self.cards)

    def deckPrint(self):
        for card in self.cards:
            print(card)

    def drawTopOfDeck(self):
        return self.cards.pop(0)

class Dealer:
    def __init__(self):
        self.cards = []

    def theFlop(self, d):
        for i in range(0,3):
            c = d.drawTopOfDeck()
            self.cards.append(c)

    def theTurn(self, d):
        self.cards.append(d.drawTopOfDeck())

    def theRiver(self, d):
        self.cards.append(d.drawTopOfDeck())

    def dealerPrintFlop(self):
        for i in range(0,3):
            print(self.cards[i])

    def dealerPrintTurn(self):
        for i in range(0,4):
            print(self.cards[i])

    def dealerPrintRiver(self):
        for i in range(0,5):
            print(self.cards[i])

    def publicCards(self):
        return self.cards

    def __str__(self):
        retVal = ''.join(str(s) for s in self.cards)
        return retVal

class Player:
    def __init__(self):
        self.evalCards = []
        self.cards = []
        self.pot = 1000;
        self.bestHand = 11

    def resetBestHand(self):
        self.bestHand = 11

    def printBestHand(self):
        print("Your best hand is a: ")
        if(self.bestHand == 1):
            print("Royal flush")
            return "a Royal Flush!"
        if(self.bestHand == 2):
            print("Straight flush")
            return "a Straight Flush!"
        if(self.bestHand == 3):
            print("Four of a Kind")
            return "a Four of a Kind!"
        if(self.bestHand == 4):
            print("Full house!")
            return "a Full House!"
        if(self.bestHand == 5):
            print("Flush!")
            return "a Flush!"
        if(self.bestHand == 6):
            print("Straight!")
            return "a Straight!"
        if(self.bestHand == 7):
            print("Three of a Kind!")
            return "a Three of a Kind!"
        if(self.bestHand == 8):
            print("Two Pair!")
            return "a Two Pair!"
        if(self.bestHand == 9):
            print("Pair!")
            return "a Pair!"
        if(self.bestHand > 9):
            print("High Card!")
            return "a High Card!"

        print("\nRank is: " + str(self.bestHand))

    def evaluateAll(self, x):
        self.resetBestHand()
        self.twoPair(x)
        self.threeOfKind(x)
        self.fourOfKind(x)
        self.pair(x)
        self.straight(x)

        self.flush(x)
        self.highCard()
        self.printBestHand()
        
        return self.bestHand

    def startingHand(self, d):
        for i in range(0,4):
            card = Card()
            card = d.drawTopOfDeck()
            self.cards.append(card)

    def sortHand(self, d):
        two = "2"
        for i in range(0,4):
            for j in range(0,4):
                if(self.cards[j].getRank() < self.cards[i].getRank()):
                    temp = self.cards[i].getRank()
                    temp1 = self.cards[j].getRank()
                    self.cards[i].setRank(temp1)
                    self.cards[j].setRank(temp)

    def evaluate(self, d):
        pass

    def twoPair(self, x):
        elements = []
        myList = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        returnList = [0, 0, 0, 0, 0, 0, 0]
        #self.evalCards.extend(self.cards)
        #self.evalCards.extend(x)
        #print(self.evalCards)
        self.evalCards = []
        elements = []
        self.evalCards.extend(self.cards)
        self.evalCards.extend(x)
        self.cards = []

        for card in self.evalCards:
            elements.append(card.getRank())

        for val in elements:
            myList[val] += 1

        #print(elements)
        retVal = None
        if 4 in elements:
            retVal = True
        else:
            retVal = False

        #for i in range(0,16):
        #    print(myList[i], sep= ' ', end='')

        pair1 = 0
        pair2 = 0
        countPair = 0
        check = 0
        k = 0
        for i in range(0,16):
            if(myList[i] >= 2 and countPair != 1):
                countPair = 1
                pair1 = i
                returnList[k] = pair1
                k += 1

            if(myList[i] >= 2 and pair1 != i and countPair == 1):
                countPair = 0
                pair2 = i
                returnList[k] = pair2
                k += 1

        print('')
        handCounter = 0
        tableCounter = 0
        a = 0
        b = 1
        i = 0
        for val in elements:
            if(i < 4):
                if val == returnList[0] or val == returnList[1]:
                    handCounter += 1
            if(i >= 4):
                if val == returnList[0] or val == returnList[1]:
                    tableCounter += 1
            if((handCounter >= 2 and tableCounter >=2) or (handCounter == 1 and tableCounter == 3)):
                i = 100
                if self.bestHand > 8:
                    self.bestHand = 8
            i += 1
        handCounter = 0
        tableCounter = 0
        a += 1
        b += 1
        hPos13Counter = 0
        tPos13Counter = 0
        i = 0
        for val in elements:
            if i < 4:
                if(val == returnList[1] or val == returnList[2]):
                    handCounter += 1
                if(val == returnList[0] or val == returnList[2]):
                    hPos13Counter += 1
            if(i >= 4):
                if(val == returnList[1] or val == returnList[2]):
                    tableCounter += 1
                if(val == returnList[0] or val == returnList[2]):
                    tPos13Counter += 1
            if((handCounter >=2 and tableCounter >= 2) or (handCounter == 1 and tableCounter == 3)):
                i = 100
                if(self.bestHand > 8):
                    self.bestHand = 8
            if((hPos13Counter >= 2 and tPos13Counter >=2) or (hPos13Counter == 1 and tPos13Counter == 3)):
                i = 100
                if(self.bestHand > 8):
                    self.bestHand = 8
            i += 1
        """
        #print(pair1)
        #print(pair2)
        #print("All possible pairs are: ")
        retVal = []
        for i in range(0,6):
            if(returnList[i] != 0):
                retVal.append(returnList[i])
                #print(returnList[i])
        
        return retVal
        """

    def straightFlush(self, x):
        pass

    def flush(self, x):
        elements = []
        stringElements = []
        myList = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        s = 0
        h = 0
        c = 0
        d = 0
        a = 0
 
        for card in self.evalCards:
            elements.append(card.getRank())

        i = 0
        for card in self.evalCards:
            cardType = card.getSuit()
            #print(cardType)
            if(cardType == "Clubs"):
                c += 1
                if(i < 4 and c > 2):
                    c = 2
            elif(cardType == "Hearts"):
                h += 1
                if(i < 4 and h > 2):
                    h = 2
            elif(cardType == "Spades"):
                s += 1
                if(i < 4 and s > 2):
                    s = 2
            elif(cardType == "Diamonds"):
                d += 1
                if(i < 4 and d > 2):
                    d = 2
            i += 1
        if(c >= 5):
            #print("Clubs flush!")
            if(self.bestHand > 5):
                self.bestHand = 5
        if(h >= 5):
            #print("Hearts flush!")
            if(self.bestHand > 5):
                self.bestHand = 5
        if(s >= 5):
            #print("Spades flush!")
            if(self.bestHand > 5):
                self.bestHand = 5
        if(d >=5):
            #print("Diamonds flush!")
            if(self.bestHand > 5):
                self.bestHand = 5

        for val in elements:
            myList[val] += 1

    def straight(self, x):
        elements = []
        myList = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        returnList = [0, 0, 0, 0, 0, 0, 0]

        for card in self.evalCards:
            elements.append(card.getRank())

        for val in elements:
            myList[val] += 1

        counter = 0
        position = 0
        i = 0
        for val in myList:
            if(myList[i] >= 1):
                counter += 1 
                if(counter >= 5):
                    position = i
            else:
                counter = 0
            if(position > 0):
                pass
            i += 1
        handCounter = 0
        tableCounter = 0
        p = position
        p1 = position - 1
        p2 = position - 2
        p3 = position - 3
        p4 = position - 4
        check = 0
        check1 = 0
        check2 = 0
        check3 = 0
        check4 = 0
        checkForFlush = 0

        i = 0
        for val in elements:
            if(i < 4):
                if(val == p and check == 0):
                    check = 1
                    handCounter += 1
                elif(val == p1 and check1 == 0):
                    check1 = 2
                    handCounter += 1
                elif(val == p2 and check2 == 0):
                    check2 = 3
                    handCounter += 1
                elif(val == p3 and check3 == 0):
                    check3 = 4
                    handCounter += 1
                elif(val == p4 and check4 == 0):
                    check4 = 5
                    handCounter += 1
            if(i >= 4):
                if(val == p):
                    check = 1
                    tableCounter += 1
                elif(val == p1):
                    check1 = 2
                    tableCounter += 1
                elif(val == p2):
                    check2 = 3
                    tableCounter += 1
                elif(val == p3):
                    check3 = 4
                    tableCounter += 1
                elif(val == p4):
                    check4 = 5
                    tableCounter += 1
            
            if(handCounter >= 2 and tableCounter >= 3):
                #print("Straight! Highest value: " + p)
                i = 100
                if(self.bestHand > 6):
                    self.bestHand = 6
                checkForFlush = 0
                for u in range(0,9):
                    checkForFlush = 0
                    for t in range(0,9):
                        if(self.evalCards[u].getRank() == self.evalCards[t].getRank() + 1):
                            if(self.evalCards[u].getSuit() == self.evalCards[t].getSuit()):
                                 checkForFlush += 1
                        if(self.evalCards[u].getRank() == self.evalCards[t].getRank() + 2):
                            if(self.evalCards[u].getSuit() == self.evalCards[t].getSuit()):
                                 checkForFlush += 1
                        if(self.evalCards[u].getRank() == self.evalCards[t].getRank() + 3):
                            if(self.evalCards[u].getSuit() == self.evalCards[t].getSuit()):
                                 checkForFlush += 1
                        if(self.evalCards[u].getRank() == self.evalCards[t].getRank() + 4):
                            if(self.evalCards[u].getSuit() == self.evalCards[t].getSuit()):
                                 checkForFlush += 1 
                        if(self.bestHand > 2 and checkForFlush >= 5):
                            #print("Straight flush!")
                            bestHand = 2

            i += 1

    def fourOfKind(self, x):
        elements = []
        myList = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        returnList = [0, 0, 0, 0, 0, 0, 0]
       
        for card in self.evalCards:
            elements.append(card.getRank())

        for val in elements:
            myList[val] += 1
 
        pair1 = 0
        pair2 = 0
        countPair = 0
        check = 0
        k = 0
        for i in range(0,16):
            if(myList[i] == 4):
                pair1 = i
                returnList[k] = pair1
                k += 1

        handCounter = 0
        tableCounter = 0
        phandCounter = 0
        ptableCounter = 0
        i = 0
        for val in elements:
            if(i < 4):
                if(val == returnList[0]):
                    handCounter += 1
                if(val == returnList[1]):
                    phandCounter += 1
            if(i >= 4):
                if(val == returnList[0]):
                    tableCounter += 1
                if(val == returnList[1]):
                    ptableCounter += 1
            compare = handCounter + tableCounter

            if(handCounter == 3 or tableCounter == 4):
                break
            elif(compare == 4 and returnList[0] > 0):
                #print("A correct 4 of a kind is: ")
                #print(returnList[0])
                i = 100
                if(self.bestHand > 3):
                    self.bestHand = 3
       
            pcompare = phandCounter + ptableCounter
            if(phandCounter == 3 and ptableCounter == 4):
                break
            elif(compare >= 4 and returnList[1] > 0):
                #print("A correct 4 of a kind is: ")
                #print(returnList[1])
                i = 100
                if(self.bestHand > 3):
                    self.bestHand = 3
            i += 1

    def highCard(self):
        maxValue = 0
        for card in self.evalCards:
            if(card.getRank() > maxValue):
                maxValue = card.getRank()
        if(self.bestHand > 10):
            self.bestHand = 10 - (maxValue/100)

    def pair(self, x):
        elements = []
        myList = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        returnList = [0, 0, 0, 0, 0, 0, 0]
        for card in self.evalCards: 
            elements.append(card.getRank())

        for val in elements:
            myList[val] += 1

        pair1 = 0
        pair2 = 0
        countPair = 0
        check = 0
        k = 0
        for i in range(0,16):
            if(myList[i] == 2):
                pair1 = i
                returnList[k] = pair1
                k += 1
        
        if(pair1 >= 2):
            returnList[0] = pair1
            #print("The highest pair is : ")
            #print(returnList[0])
            if(self.bestHand > 9):
                self.bestHand = 9

    def fullHouse(self, x):
        pass

    def threeOfKind(self, x):
        elements = []
        myList = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        returnList = [0, 0, 0, 0, 0, 0, 0]
        returnListPair = [0, 0, 0, 0, 0, 0, 0]

        for card in self.evalCards:
            elements.append(card.getRank())

        for val in elements:
            myList[val] += 1

        pair1 = 0
        pair2 = 0
        countPair = 0
        check = 0
        k = 0
        for i in range(0, 16):
            if(myList[i] == 3):
                pair1 = i
                returnList[k] = pair1
                k += 1

        
        handCounter = 0
        tableCounter = 0
        phandCounter = 0
        ptableCounter = 0

        i = 0
        for val in elements:
            if(i < 4):
                if(val == returnList[0]):
                    handCounter += 1
                if(val == returnList[1]):
                    phandCounter += 1
            if(i >= 4):
                if(val == returnList[0]):
                    tableCounter += 1
                if(val == returnList[1]):
                    ptableCounter += 1

            compare = handCounter + tableCounter
            if((handCounter == 3 and tableCounter == 0) or (handCounter == 4 and tableCounter == 0)):
                break
            elif(compare >= 3 and returnList[0] > 0):
                #print("A correct 3 of a kind is: ")
                #print(returnList[0])
                i = 100
                if(self.bestHand > 7):
                    self.bestHand = 7
            pcompare = phandCounter + ptableCounter
            if((phandCounter == 3 and ptableCounter == 0) or (phandCounter == 4 and ptableCounter == 0)):
                break
            elif(compare >= 3 and returnList[1] > 0):
                i = 100
                if(self.bestHand > 7):
                    self.bestHand = 7
            i += 1
        HC = handCounter
        TC = tableCounter
        k = 0
        for i in range(0,16):
            if(myList[i] == 2):
                pair1 = i
                returnList[k] = pair1
                k += 1
        i = 0
        for p in range(0,5):
            resetHand = HC
            resetTable = TC
            for val in elements:
                if(i < 4):
                    if(val == returnListPair[p]):
                        resetHand += 1
                if(i >= 4):
                    if(val == returnListPair[p]):
                        resetTable += 1
                if(resetHand == 2 and resetTable == 3):
                    #print("We have full house!")
                    i = 100
                    if(self.bestHand > 4):
                        self.bestHand = 4
                i += 1
        
    def printHand(self):
        for i in range(0,4):
            print(self.cards[i], sep=', ', end= '')

class Evaluator:
    def __init__(self):
        self.cards = []

    def sort(self, d):
        pass

if __name__ == "__main__":

    c = Card()
    player = []
    print("\nWelcome to poker!")
    num = int(raw_input("How many players? (1-5)>> "))
    for i in range(0,num):
        print("Player: " + str(i + 1) + " created")
        player.append(Player())
    
    playAgain = 1
    myPot = 1000
    while playAgain != 0:
        bet = 0
        totalBets = 0
        call = 0
        foldFlag = []
        for i in range(0,num):
            foldFlag.append(0)

        deck = Deck()
        dealer = Dealer()
        print("\nLets play some poker!")
        for j in range(0,num):
            print("Player: " + str(j + 1))
            player[j].startingHand(deck)
            player[j].sortHand(deck)
            player[j].printHand()
            print("\n")
 
        print("Your current amount of cash is: " + str(player[0].pot))
        if(foldFlag[0] == 0):
            bet = int(raw_input("How much would you like to bet or fold(0)?>> "))
        if(bet > 0 and foldFlag[0] == 0):
            player[0].pot -= bet
            totalBets += bet
        else:
            bet = 25
            foldFlag[0] = 1

        for j in range(1,num):
            player[j].pot -= bet
            totalBets += bet

        dealer.theFlop(deck)
        dealer.dealerPrintFlop()
        print("Your current amount of cash is: " + str(player[0].pot))
        if(foldFlag[0] == 0):
            bet = int(raw_input("How much would you like to bet or fold(0)?>> "))

        if(bet > 0 and foldFlag[0] == 0):
            player[0].pot -= bet
            totalBets += bet
        else:
            bet = 50
            foldFlag[0] = 1

        for j in range(1,num):
            player[j].pot -= bet
            totalBets += bet

        dealer.theTurn(deck)
        dealer.dealerPrintTurn()
        print("Your current amount of cash is: " + str(player[0].pot))
        if(foldFlag[0] == 0):
            bet = int(raw_input("How much would you like to bet or fold(0)?>> "))

        if(bet > 0 and foldFlag[0] == 0):
            player[0].pot -= bet
            totalBets += bet
        else:
            bet = 25
            foldFlag[0] = 1

        for j in range(1,num):
            player[j].pot -= bet
            totalBets += bet
  
        dealer.theRiver(deck)
        dealer.dealerPrintRiver()
        print("Your current amount of cash is: " + str(player[0].pot))
        if(foldFlag[0] == 0):
            bet = int(raw_input("How much would you like to bet or fold(0)?>> "))

        if(bet > 0 and foldFlag[0] == 0):
            player[0].pot -= bet
            totalBets += bet
        else:
            bet = 50
            foldFlag[0] = 1

        for j in range(1,num):
            player[j].pot -= bet
            totalBets += bet

        winner = 11
        winningPlayer = 0
        temp = 11
        fcp = 0
        if(foldFlag[0] == 1):
            fcp = 1
        while(fcp < num):
            print("********************************")
            print("Player: " + str(fcp))
            temp = player[fcp].evaluateAll(dealer.publicCards())
            print("********************************")
            if(winner > temp):
                winner = temp
                winningPlayer = fcp
                print("fcp: " + str(fcp) )
            fcp += 1
        player[winningPlayer].pot += totalBets
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        print("$\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        print("\nThe winning player is: Player: " + str(winningPlayer + 1))
        #print("Wins with rank: " + str(winner) + "\n")
        player[winningPlayer].printBestHand()
        for j in range(0, num):
            print("Player: " + str(j + 1) + " cash: " + str(player[j].pot))

        playAgain = int(raw_input("\nEnter the number 0 to quit. Enter any number to keep playing: "))
        for p in player:
            p.bestHand = 11
            p.cards = []
            p.evalCards = []
    """
    c = Card()
    print("\nWelcome to poker!")
    player1 = Player()
    player2 = Player()
    dealer = Dealer()
    deck = Deck()

    c = deck.drawTopOfDeck()

    player1.startingHand(deck)
    player2.startingHand(deck)
    player1.printHand()

    player1.sortHand(deck)
    print("\n\nPlayer 1 has: ")
    player1.printHand()

    print("\n\nThe flop is: ")
    dealer.theFlop(deck)
    dealer.dealerPrintFlop()
    print("\nThe turn is: ")
    dealer.theTurn(deck)
    dealer.dealerPrintTurn()
    print("\nThe river is: ")
    dealer.theRiver(deck)
    dealer.dealerPrintRiver()
    player1.evaluate(deck)

    player1.evaluateAll(dealer.publicCards())
    #print("\nYOOOO")
    
    print(dealer)
    twoPairs = player1.twoPair(dealer.publicCards())
    for pair in twoPairs:
        print(pair)
    print('')
    """


