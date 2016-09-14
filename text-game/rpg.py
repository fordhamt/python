"""Paul Fordham | ptf06c """
#!/user/bin/env python
from __future__ import print_function # self.request.send()
import SocketServer
import threading
import random

class Character():
    def __init__(self):
        self.maxHP = 0
        self.strength = 0
        self.defense = 0

class Player(Character):
    def __init__(self):
        Character.__init__(self)
	self.strength = 0
        self.defense = 0
        self.maxHP = 0
        self.HP = 0
        self.isDone = False
        self.isAttacking = False
        self.name = "Default"

    def help(self):
        return "go [N,S,E,or W]\nquit\nattack\nhealth\nhelp\n"

    def health(self):
        return self.name + " has " + str(self.HP) + " HP.\n"

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
            return self.name + " doesn't see anything worth attacking.\n"
        else:
            damage = random.randint(0, 6) + self.strength - opponent.defense
            retVal = ''
            if damage <= 0:
                retVal = opponent.name + " evades " + self.name + "'s attack.\n"
            else:
                opponent.HP = opponent.HP - damage
                retVal = retVal + self.name + " attacks " + opponent.name + " for " + str(damage) + " points of damage!\n"
            damage = random.randint(0, 6) + opponent.strength - self.defense
            if damage <= 0:
                retVal = retVal + self.name + " evades " + opponent.name + "'s attack.\n"
            else:
                self.HP = self.HP - damage
                retVal = retVal + opponent.name + " attacks " + self.name + " for " + str(damage) + " points of damage!\n"
            return retVal
    def quit(self):
        self.isDone = True
        return self.name + " has lost all hope and locked themself in the ACM office to read ACM magazines and await their final doom.\n"

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

class ThreadedTCPRequestHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        """
        def printBoard(board):
            for i in range(25):
                if i % 5 == 0:
                    self.request.send("\n")
                self.request.send(str(board[i]))
        """
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

        opponent = EvilRobot()
        robot1 = EvilRobot()
        robot2 = EvilRobot()
        robot3 = EvilRobot()
        robot4 = EvilRobot()

        self.request.send("Enter your character's name: ")
        #name = raw_input()
        name = self.request.recv(2048).strip()

        self.request.send("Are you a CodeWarrior or 1337H4x0r? Enter [c] or [h]: ")
        #classChoice = raw_input()
        classChoice = self.request.recv(4)[0]

        self.request.send("It's a dark and stormy night. One unfortunate Computer Science student has fallen   asleep on the Love 105 suites couch while cramming for their upcoming final. They head down to the Majors Lab to gather their belongings before heading home. They approach the lab and encounter a strange sight: the lab is empty and dark...but the door is open. The power must have been knocked out by the storm. The brave little CS student enters the dark room to find their backpack...\n")

        if classChoice == 'c':
            player = CodeWarrior(name)
        else:
            player = H4x0r(name)

        #printBoard(board)
        while not player.isDone:
            #choice = raw_input("> ")
            self.request.send("> ")
            #choice = self.request.recv(2048)
            #self.request.send("> sent: " + choice)
            choice = self.request.recv(2048).strip()
            if choice == 'help':
                out = player.help()
                self.request.send(out)
            if choice == 'go N' or choice == 'go S' or choice == 'go E' or choice == 'go W':
                move = player.go(choice)
                square = pos + move
                if player.isAttacking:
                    self.request.send(player.name + " can't run from the Evil Robot.\n")
                elif square < 0 or square > 24:
                    self.request.send(player.name + " has run into a wall. Try another direction.\n")
                elif choice == 'go W' and (pos == 0 or pos == 5 or pos == 10 or pos == 15 or pos == 20):
                    self.request.send(player.name + " has run into a wall. Try another direction.\n")
                elif choice == 'go E' and (pos == 4 or pos == 9 or pos == 14 or pos == 19 or pos == 24):
                    self.request.send(player.name + " has run into a wall. Try another direction.\n")
                elif choice == 'go N' and (pos == 0 or pos == 1 or pos == 2 or pos == 3 or pos == 4):
                    self.request.send(player.name + " has run into a wall. Try another direction.\n")
                elif choice == 'go S' and (pos == 20 or pos == 21 or pos == 22 or pos == 23 or pos == 24):
                    self.request.send(player.name + " has run into a wall. Try another direction.\n")
                elif board[square] == 0:
                    board[pos] = 0
                    board[square] = 1
                    pos = square
                elif board[pos + move] == 2:
                    self.request.send(player.name + " has encountered an Evil Robot. It appears to have assembled itself out of spare parts. Prepare to fight!\n")
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
                    self.request.send(player.name + " ran into one of those legendary mechanical rat traps in the Love basement. RIP.\n")
                elif board[square] == 4:
                    player.isDone = True
                    self.request.send("Congratulations, " + player.name + " found their backpack!!!\n")
                    self.request.send("And so, our hero safely makes their way to the exit. Luckily, " + player.name + " made it out alive this time. But one thing is for sure " + player.name + " will never put off studying for their final exams ever again.\n")
        
            if choice == 'quit':
                out = player.quit()
                self.request.send(out)
            if choice == 'attack':
                out = player.attack(opponent)
                self.request.send(out)
                if player.HP <= 0:
                    self.request.send(player.name + "'s epic backpack search has come to an end. RIP.\n")
                    player.isDone = True
                elif opponent.HP <= 0 and player.isAttacking:
                    player.isAttacking = False
                    self.request.send("Evil Robot has crashed! " + player.name + " wins!\n")
                    board[pos] = 0
                    board[square] = 1
                    pos = square
            if choice == 'health':
                out = player.health()
                self.request.send(out)
        self.request.close()

class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass

if __name__ == "__main__":
    HOST, PORT = "localhost", 9000
    server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.start()
