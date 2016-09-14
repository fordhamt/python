"""Paul Fordham | ptf06c """
#!/user/bin/env python
from __future__ import print_function # print()
from socket import *
import random

class Character:
    def __init__(self):
        self.maxHP = 0
        self.strength = 0
        self.defense = 0

class Player(Character):
    def __init__(self):
        Character.__init__(self)
        self.HP = 0
        self.isDone = False
        self.isAttacking = False
        self.name = "Default"

    def help(self):
        print("go [N,S,E,or W]\nquit\nattack\nhealth\nhelp")

    def health(self):
        print(self.name + " has " + str(self.HP) + " HP.")

    def go(self, direction):
        if direction == 'go N':
            return -5
        if direction == 'go S':
            return 5
        if direction == 'go E':
            return 1
        if direction == 'go W':
            return -1

    def attack(self, opponent):
        if not self.isAttacking:
            print(self.name + " doesn't see anything worth attacking.")
        else:
            damage = random.randint(0, 6) + self.strength - opponent.defense
            if damage <= 0:
                print(opponent.name + " evades " + self.name + "'s attack.")
            else:
                opponent.HP = opponent.HP - damage
                print(self.name + " attacks " + opponent.name + " for " + str(damage) + " points of damage!")
            damage = random.randint(0, 6) + opponent.strength - self.defense
            if damage <= 0:
                print(self.name + " evades " + opponent.name + "'s attack.")
            else:
                self.HP = self.HP - damage
                print(opponent.name + " attacks " + self.name + " for " + str(damage) + " points of damage!")

    def quit(self):
        self.isDone = True
        print(self.name + " has lost all hope and locked themself in the ACM office to read ACM magazines and await their final doom.")

class EvilRobot(Character):
    def __init__(self):
        Character.__init__(self)
        self.name = "Evil Robot"
        self.maxHP = 15
        self.HP = 15
        self.strength = 9
        self.defense = 7

class CodeWarrior(Player):
    def __init__(self, name):
        Player.__init__(self)
        self.name = name
        self.maxHP = 30
        self.HP = 30
        self.strength = 10
        self.defense = 8

class H4x0r(Player):
    def __init__(self, name):
        Player.__init__(self)
        self.name = name
        self.maxHP = 30
        self.HP = 30
        self.strength = 8
        self.defense = 10

board = []
for i in range(25):
    board.append(0)

board[10] = 1
pos = 10
"""
player == 1
enemy  == 2
rat    == 3
backpack == 4
"""
enemy1 = random.randint(0,24)
enemy2 = random.randint(0,24)
enemy3 = random.randint(0,24)
enemy4 = random.randint(0,24)
backpack = random.randint(0,24)
rat = random.randint(0,24)

settingUp = True
if board[enemy1] == 0:
    board[enemy1] = 2
else:
    while settingUp:
        enemy1 = random.randint(0,24)
        if board[enemy1] == 0:
            board[enemy1] = 2
            settingUp = False
settingUp = True
if board[enemy2] == 0:
    board[enemy2] = 2
else:
    while settingUp:
        enemy2 = random.randint(0,24)
        if board[enemy2] == 0:
            board[enemy2] = 2
            settingUp = False
settingUp = True
if board[enemy3] == 0:
    board[enemy3] = 2
else:
    while settingUp:
        enemy3 = random.randint(0,24)
        if board[enemy3] == 0:
            board[enemy3] = 2
            settingUp = False
settingUp = True
if board[enemy4] == 0:
    board[enemy4] = 2
else:
    while settingUp:
        enemy4 = random.randint(0,24)
        if board[enemy4] == 0:
            board[enemy4] = 2
            settingUp = False
settingUp = True
if board[rat] == 0:
    board[rat] = 3
else:
    while settingUp:
        rat = random.randint(0,24)
        if board[rat] == 0:
            board[rat] = 3
            settingUp = False
settingUp = True
if board[backpack] == 0:
    board[backpack] = 4
else:
    while settingUp:
        backpack = random.randint(0,24)
        if board[backpack] == 0:
            board[backpack] = 4
            settingUp = False

def printBoard(board):
    for i in range(25):
        if i % 5 == 0:
            print("\n", end ='')
        print(board[i], sep=' ',end ='')
print("")
opponent = EvilRobot()
robot1 = EvilRobot()
robot2 = EvilRobot()
robot3 = EvilRobot()
robot4 = EvilRobot()

print("Enter your character's name: ", end='')
name = raw_input()

print("Are you a CodeWarrior or 1337H4x0r? Enter [c] or [h]: ", end='')
classChoice = raw_input()

print("It's a dark and stormy night. One unfortunate Computer Science student has fallen asleep on the Love 105 suites couch while cramming for their upcoming final. They head down to the Majors Lab to gather their belongings before heading home. They approach the lab and encounter a strange sight: the lab is empty and dark...but the door is open. The power must have been knocked out by the storm. The brave little CS student enters the dark room to find their backpack...")

if classChoice == 'c':
    player = CodeWarrior(name)
else:
    player = H4x0r(name)

printBoard(board)
print('')
while not player.isDone:
    choice = raw_input("> ")
    if choice == 'help':
        player.help()
    if choice == 'go N' or choice == 'go S' or choice == 'go E' or choice == 'go W':
        move = player.go(choice)
        square = pos + move
        if player.isAttacking:
            print(player.name + " can't run from the Evil Robot.")
        elif square < 0 or square > 24:
            print(player.name + " has run into a wall. Try another direction.")
        elif choice == 'go W' and (pos == 0 or pos == 5 or pos == 10 or pos == 15 or pos == 20):
            print(player.name + " has run into a wall. Try another direction.")
        elif choice == 'go E' and (pos == 4 or pos == 9 or pos == 14 or pos == 19 or pos == 24):
            print(player.name + " has run into a wall. Try another direction.")
        elif choice == 'go N' and (pos == 0 or pos == 1 or pos == 2 or pos == 3 or pos == 4):
            print(player.name + " has run into a wall. Try another direction.")
        elif choice == 'go S' and (pos == 20 or pos == 21 or pos == 22 or pos == 23 or pos == 24):
            print(player.name + " has run into a wall. Try another direction.")
        elif board[square] == 0:
            board[pos] = 0
            board[square] = 1
            pos = square
            printBoard(board)
            #print('moving \n')
        elif board[pos + move] == 2:
            print(player.name + " has encountered an Evil Robot. It appears to have assembled itself out of spare parts. Prepare to fight!")
            player.isAttacking = True
            if square == enemy1:
                opponent = robot1
            elif square == enemy2:
                opponent = robot2
            elif square == enemy3:
                opponent = robot3
            elif square == enemy4:
                opponent = robot4
        elif board[square] == 3:
            player.isDone = True
            print(player.name + " ran into one of those legendary mechanical rat traps in the Love basement. RIP.")
        elif board[square] == 4:
            player.isDone = True
            print("Congratulations, " + player.name + " found their backpack!!!")
            print("And so, our hero safely makes their way to the exit. Luckily, " + player.name + " made it out alive this time. But one thing is for sure " + player.name + " will never put off studying for their final exams ever again.")
        else:
            print(str(pos + move))
            printBoard(board)
            print('')
    if choice == 'quit':
        player.quit()
    if choice == 'attack':
        player.attack(opponent)
        if player.HP <= 0:
            print(player.name + "'s epic backpack search has come to an end. RIP.")
            player.isDone = True
        elif opponent.HP <= 0:
            player.isAttacking = False
            print("Evil Robot has crashed! " + player.name + " wins!")
            board[pos] = 0
            board[square] = 1
            pos = square
            printBoard(board)
            print('')
    if choice == 'health':
        player.health()
