#!/usr/bin/env python

from __future__ import print_function
#import random
import sys, os
#import time
from PyQt5 import QtWidgets, QtCore, QtGui
from Poker import *

"""Module will setup the gui for poker game, calling items from 'Poker.py,' maintains main game loop"""

class Poker_Window(QtWidgets.QMainWindow):
	"""Poker_Window sets up the main window of the game and creates the items for the game (self.poker_game = Poker_Game(self)), 
		a very simple menu is also included with an exit button."""
	def __init__(self):
		QtWidgets.QMainWindow.__init__(self)
		#self.resize(100, 100)
		self.setup()

	def setup(self):
		self.setWindowTitle("Omaha Poker")

		self.poker_game = Poker_Game(self)
		self.setCentralWidget(self.poker_game)
                """
		exit_action = QtWidgets.QAction('Exit', self)
		exit_action.triggered.connect(QtWidgets.qApp.quit)

		menu_bar = self.menuBar()
		menu_bar.setNativeMenuBar(False)
		file_menu = menu_bar.addMenu('File')
		file_menu.addAction(exit_action)
                """
		self.show()

class Poker_Game(QtWidgets.QWidget):
	def __init__(self, parent):
		"""'__init__' sets up the basics of the game including the background color and instantiating the players. It then combines
			the players into a list for easy iteration in some instances and finishes by calling 'setup()' to complete setup of the game."""
		QtWidgets.QWidget.__init__(self, parent)
		p = self.palette()
		p.setColor(self.backgroundRole(), QtGui.QColor(40, 128, 40))
		self.setPalette(p)
		self.setAutoFillBackground(True)
		#create all players in init so that setup can be called whenever board needs to be reset for next hand
		self.player = Player()
		self.cpu1 = Player()
		self.cpu2 = Player()
		self.cpu3 = Player()
		self.playerList = [self.player, self.cpu1, self.cpu2, self.cpu3]
		self.setup()

	def setup(self, num=None):		#num flag is to check whether layout has already been set, setup_next_hand will set this variable
		"""Setup function deals with the bulk of setting everything needed for the game and linking buttons to their SLOTS.
			Players are not initialized in setup to avoid resetting their cash values. All other needed items are reset to updated
			values in setup(). The Dealer is reinitialized anytime that setup() is called, negating any chance of the dealer 
			holding on to cards from the previous hand. The optional 'num' flag for 'setup()' is used to determine whether setup has
			yet been called. This is because if it has the grid has already been set as the layout and does not need to be set again.
			The 'num' flag provides no other utility to this method."""
		self.deck = Deck()
		self.main_pot = 0			#this is the pot all bets contribute to
		self.current_bet = 0		#used to check what the current high bet that must be called is
		self.bet_raised = False		#know whether there needs to be another round of betting before dealing more cards
		self.flop_shown = False		#[flop, turn, river]_shown flags help determine which action needs to be taken next
		self.turn_shown = False
		self.river_shown = False

		#deal hands to each player to setup the game
		for x in self.playerList:
			x.startingHand(self.deck)

		#now initialize the dealer:
		self.dealer = Dealer()
		self.dealer.theFlop(self.deck)
		#burn card
		self.deck.drawTopOfDeck()
		self.dealer.theTurn(self.deck)
		#burn card
		self.deck.drawTopOfDeck()
		self.dealer.theRiver(self.deck)
		#dealer's cards are now set, set up the images for the cards
		self.dealerCardImages = []
		for x in self.dealer.cards:
			card = convert(x)
			#card.setAlignment(QtCore.Qt.AlignLeft)
			self.dealerCardImages.append(card)

		#generate the images for card in each player's hand, images are on QLabels
		self.singlePlayerCardImages = []		#stores a list of card images for individual player
		self.allPlayerCardImages = []			#stores list of lists, each nested list coresponds to a player's cards
		for i in self.playerList:
			for x in i.cards:
				card = convert(x)
				self.singlePlayerCardImages.append(card)					#add the card to the list of cards in the player's hand
			self.allPlayerCardImages.append(self.singlePlayerCardImages)	#append the hand to the all list
			self.singlePlayerCardImages = [] 								#reset to empty list to prepare for next player's hand 

		#add all the cards to the table
		#computers each have two cards face down, player has all cards face up
		#convert is called for the 3rd and 4th cards of each cpu player so that a cardback label is returned to be added
		if not num:
			self.grid = QtWidgets.QGridLayout()
			self.setLayout(self.grid)
		count = 2	#count resets to 1 after each player is printed
		for x in self.allPlayerCardImages[0]:	#human player
			self.grid.addWidget(x, 7, count+1, 1, 1)
			count += 1	
		count = 1	
		for x in self.allPlayerCardImages[1]:	#cpu1, left side of board
			if count < 3:
				self.grid.addWidget(x, count+1, 1, 1, 1)
			else:
				self.grid.addWidget(convert(), count+1, 1, 1, 1)
			count += 1
		count = 2
		for x in self.allPlayerCardImages[2]:	#cpu2, top of board
			if count < 4:
				self.grid.addWidget(x, 1, count+1, 1, 1)
			else:
				self.grid.addWidget(convert(), 1, count+1, 1, 1)
			count += 1
		count = 1
		for x in self.allPlayerCardImages[3]:	#cpu3, right side of board
			if count < 3:
				self.grid.addWidget(x, count+1, 10, 1, 1)
			else:
				self.grid.addWidget(convert(), count+1, 10, 1, 1)
			count += 1


		#next creating labels for each player:
		######need to come back to this and add remaining cash to this#####
		self.humanLabel = Player_Label(self, "You", self.player.pot)
		self.cpu1Label = Player_Label(self, "CPU 1", self.cpu1.pot)
		self.cpu2Label = Player_Label(self, "CPU 2", self.cpu2.pot)
		self.cpu3Label = Player_Label(self, "CPU 3", self.cpu3.pot)
		self.main_pot_label = Player_Label(self, "POT", self.main_pot)

		#add the labels to the layout
		self.grid.addWidget(self.humanLabel, 6, 3, 1, 2)
		self.grid.addWidget(self.cpu1Label, 5, 2, 1, 2)
		self.grid.addWidget(self.cpu2Label, 2, 3, 1, 2)
		self.grid.addWidget(self.cpu3Label, 5, 6, 1, 2)
		self.grid.addWidget(self.main_pot_label, 4, 4, 1, 2)

		###currently does not act as fold, needs is active player attribute, rest of hand will play through automatically###
		###fold currently acts as a re-deal with no further changes made to state of game###
		self.fold = QtWidgets.QPushButton("Fold")
		self.fold.clicked.connect(lambda: self.setup_next_hand())
		self.grid.addWidget(self.fold, 7, 2, 1,1)

		self.bet = QtWidgets.QPushButton("Place Bet!")
		self.bet.clicked.connect(lambda: self.place_bet())
		self.grid.addWidget(self.bet, 6, 7, 1, 1)

		#creating a button that will be used when the winner is shown to move to next hand
		self.next_hand = QtWidgets.QPushButton("Next Hand")
		self.next_hand.clicked.connect(lambda: self.setup_next_hand())

		self.user_bet_entry = QtWidgets.QLineEdit()
		self.user_bet_entry.setToolTip("Enter your bet here!")
		self.user_bet_entry.setFixedWidth(75)
		self.user_bet_entry.returnPressed.connect(lambda: self.place_bet())
		self.grid.addWidget(self.user_bet_entry, 7, 7, 1, 1)
		self.user_bet_entry.setFocus()

		self.check_button = QtWidgets.QPushButton("Check")
		self.check_button.clicked.connect(lambda: self.check_clicked())
		self.grid.addWidget(self.check_button, 6, 2, 1, 1)

		self.call_button = QtWidgets.QPushButton("Call")
		self.call_button.clicked.connect(lambda: self.call_clicked())
		self.grid.addWidget(self.call_button, 7, 1, 1, 1)

	def setup_next_hand(self):
		"""This must be called all the end of each hand to clear player hands and prepare for new cards,
			also removes current card images from the grid so they can be redrawn with new values
			Dealer does not need to be cleared or dealt with, new dealer just constructed in setup.
			To prepare for setup(), the main grid is cleared of all widgets, and all of the player's cards are cleared by
			setting the card attributes to empty lists."""
		#clear all players hands
		for x in self.playerList:
			x.cards = []

		#clear all widgets from grid, they will be redrawn in setup
		while self.grid.count():
			child = self.grid.takeAt(0)
			child.widget().setParent(None)

		#cleanup done, calling setup to reinitialize:
		self.setup(1)

	def place_bet(self):
		"""'place_bet' is called anytime a bet is made. This function stills needs functionality for CPU betting added in and is 
			not complete. Currently, it first checks that a bet was entered into the 'user_bet_entry' QLineEdit.
			If no entry was mode it resets focus to the field and does not change the state of the game except to clear the field.
			If the bet entered was not at least enough to match the current high bet, the field is again cleared and the user must enter
			a valid bet. If the bet was greater than the current high bet, the 'bet_raised' flag is set so that once CPU betting is
			enabled, the game will know it needs to cycle fully through the players for betting following the current player. If bet was 
			not greater but matches, self.bet_raised is set to False, indicating that betting will not need to cycle past that player.
			For both cases where the bet is valid, the amount of the bet is deducted from the user's cash and added in to the main_pot.
			The text labels for the user and the main_pot are then updated as needed. The call to 'show_next_card()' at the end 
			is used to determine the next state of the game."""
		if self.user_bet_entry.text() == "":		#checks no bet entered, user must check not use bet for no bet
			self.user_bet_entry.clear()
			self.user_bet_entry.setFocus()
			return
		bet = int(self.user_bet_entry.text())
		if bet < self.current_bet:			#user must at least match the current bet
			self.user_bet_entry.clear()
			self.user_bet_entry.setFocus()
			return
		if bet > self.current_bet:
			self.current_bet = bet 			#set the new high bet
			self.bet_raised = True			#flag that other users must call
			self.player.pot -= bet 			#subtract the bet from the users pot
			self.main_pot += bet 			#and add it in to the main pot
			###there will need to be functionality here for the computer to place its bets###
		else:
			self.player.pot -= bet 
			self.main_pot += bet 
			self.bet_raised = False
			####implement CPU betting####
		#simple cpu betting, cpu's will all match the player's bet no matter what
		self.cpu1.pot -= bet
		self.cpu2.pot -= bet
		self.cpu3.pot -= bet
		for _ in range(3):
			self.main_pot += bet
		#update text labels following bet for the player and the pot
		self.user_bet_entry.clear()
		self.humanLabel.setText("You: $" + str(self.player.pot))
		self.cpu1Label.setText("CPU 1: $" + str(self.cpu1.pot))
		self.cpu2Label.setText("CPU 2: $" + str(self.cpu2.pot))
		self.cpu3Label.setText("CPU 3: $" + str(self.cpu3.pot))
		self.main_pot_label.setText("POT: $" + str(self.main_pot))
		
		self.show_next_card()
	
	def check_clicked(self):
		"""Function called when 'Check' button is clicked in the main game, if a check is allowed, gameplay proceeds; 
			if a check is not allowed, game state stays the same and user must bet or fold."""
		if self.current_bet > 0:
			self.user_bet_entry.setFocus()
			return
		else:
			#######need betting for CPU players to implement rest of betting turns#####
			self.show_next_card()

	def call_clicked(self):
		"""Function called when 'Call' button is clicked in the main game. The function first checks whether a call is a valid move;
			ie. there is a 'current_bet' > 0. If call is not a valid move the function returns and game state remains the same. If it 
			is a valid move however, the current bet will be deducted from the player's cash and added to the main_pot."""
		if self.current_bet == 0:
			self.user_bet_entry.setFocus()
			return
		self.player.pot -= self.current_bet
		self.main_pot += self.current_bet
		self.bet_raised = False

			####additional code needed to allow for passing betting to CPU######
		
		self.show_next_card()

	def show_next_card(self):
		"""Quick function for convenience of showing the next card from the dealer without duplicating code"""
		if not self.flop_shown:
			self.show_flop()
		elif not self.turn_shown:
			self.show_turn()
		elif not self.river_shown:
			self.show_river()
		else:
			self.show_winner()	

	def show_flop(self):
		"""'show_flop()' reveals the first three cards from the dealer's hand, resets the current bet as we are starting a new round of 
			betting, and sets the 'self.flop_shown' flag to True."""
		for i in range(3):
			self.grid.addWidget(self.dealerCardImages[i], 3, i+3, 1, 1)
		self.current_bet = 0		#reset the current bet for next round
		self.flop_shown = True

	def show_turn(self):
		"""'show_turn()' reveals the next card in the dealer's hand by adding the widget to the grid. 'current_bet' is then reset,
			and 'self.turn_shown' is flagged as True"""
		self.grid.addWidget(self.dealerCardImages[3], 3, 6, 1, 1)
		self.current_bet = 0 		#resetting bet for next round
		self.turn_shown = True

	def show_river(self):
		"""'show_river()' reveals the final card in the dealer's hand by adding the widget to the grid. 'current_bet' is reset for final
			round of betting on this hand, and finally 'self.river_shown' is set to True."""
		self.grid.addWidget(self.dealerCardImages[4], 3, 7, 1, 1)
		self.current_bet = 0		#reset bet
		self.river_shown = True

	def show_winner(self):
		"""##Function Does Not Currently Work As Designed##Additionally functionality is needed in the evaluation running in 'Poker.py'##
			Show winner first calls a method to evaluate the player's hands. These values are then compared to see who had the best hand.
			Once the winner is known, the screen is redrawn to show the dealer's hand, the winner's hand, and a message showing the 
			winner's name and their total cash. A QPushButton is added to the bottom of the screen to allow the player
			to move to the next deal when they are ready."""
		pass
		#first generate best hands for each player
		bestHands = []
		for x in self.playerList:
			bestHands.append(x.evaluateAll(self.dealer.publicCards()))
		#check who got the best score
		#############index of winner currently defaulting to 0(human) since not all checks implented##########
#		index_of_winner = 0
#		curr_index = 0
#		for x in self.playerList:
#			for y in self.playerList:
#				print(x.bestHand)
#				print(y.bestHand)
#				if x.bestHand < y.bestHand:
#					index_of_winner = curr_index
#					print(index_of_winner)
#			curr_index += 1
		for i in bestHands:
			print(i)
		winning_value = min(bestHands)
		count = 0
		for i in self.playerList:
			if winning_value == i.bestHand:
				break
			count += 1
		
		won_with = self.playerList[count].printBestHand()
		
		#update winner's pot to reflect winnings:
		self.playerList[count].pot += self.main_pot
		self.main_pot = 0
		##remove all items from display and present the winner's hand as well as the dealer's full hand, will
		##also add a label to the screen with a congratulatory message for the winner:
		
		while self.grid.count():
			child = self.grid.takeAt(0)
			child.widget().setParent(None)
		#show dealer cards on top
		for x in range(5):
			self.grid.addWidget(self.dealerCardImages[x], 1, x, 1, 1)
			if x < 4:
				self.grid.addWidget(self.allPlayerCardImages[count][x], 2, x, 1, 1)
			#print name of the winner
		if count == 0:
			self.humanLabel = Player_Label(self, "You Won with "+won_with+"\nYour Total Cash is", self.player.pot)
			self.grid.addWidget(self.humanLabel, 3, 1, 1, 3)
		elif count == 1:
			self.cpu1Label = Player_Label(self, "CPU 1 Won with "+won_with+"\nCPU 1's Total Cash is", self.cpu1.pot)
			self.grid.addWidget(self.cpu1Label, 3, 1,1,3)
		elif count == 2:
			self.cpu2Label = Player_Label(self, "CPU 2 Won with "+won_with+"\nCPU 2's Total Cash is", self.cpu2.pot)
			self.grid.addWidget(self.cpu2Label, 3, 1, 1, 3)
		elif count == 3:
			self.cpu3Label = Player_Label(self, "CPU 3 Won with "+won_with+"\nCPU 3's Total Cash is", self.cpu3.pot)
			self.grid.addWidget(self.cpu3Label, 3, 1, 1, 3)

		self.grid.addWidget(self.next_hand, 4, 1,1,3)



def convert(card=None):
	"""if a card is not passed in to convert, convert returns a label with the cardback
		if a card is passed in, convert pulls a pixmap for the entered card and returns it as a label"""
	card_image = QtWidgets.QLabel()
	card_image.setAlignment(QtCore.Qt.AlignCenter)
	if card == None:
		image = QtGui.QPixmap("data/cardback.png")
		image = image.scaledToHeight(100)
		card_image.setPixmap(image)
		return card_image
	#need to convert card values to prepare to pull images
	s = card.getSuit()
	r = card.getRank()

	#set rank to a string value, will be concatenated with suit to pull pixmap
	if r < 11:
		r = str(r)
	if r == 11:
		r = "J"
	elif r == 12:
		r = "Q"
	elif r == 13:
		r = "K"
	elif r == 14:
		r = "A"
	#set suit to a single char
	s = s[0]
	#pull image and set as a pixmap here
	image = QtGui.QPixmap("data/"+r+s+".png")
	image = image.scaledToHeight(100)
	card_image.setPixmap(image)
	return card_image

class Player_Label(QtWidgets.QLabel):
	"""The Player_Label class is used as a wrapper for setting up uniformly formatted QLabels, without needing to specify formatting
		for each label manually."""
	def __init__(self, parent, text, cash):
		QtWidgets.QLabel.__init__(self, parent)
		self.setText(text + ": $" + str(cash))
		self.setAlignment(QtCore.Qt.AlignLeft)
		self.setStyleSheet("color: black; font-size: 24px; font-family: Calibri")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = Poker_Window()
    app.exec_()
