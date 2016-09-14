"""Paul Fordham | ptf06c """
#!/user/bin/env python
from __future__ import print_function # print()
import random  # dice roller
import enchant # dictionary

# setup helper functions
def points(w):
    if (len(w) == 3) or (len(w) == 4):
        return 1
    elif (len(w) == 5):
        return 2
    elif (len(w) == 6):
        return 3
    elif (len(w) == 7):
        return 5
    elif (len(w) > 8):
        return 11

def inGame(w, letters):
    modList = []
    posList = []
    #for letter in w:
#	posList.append(letters.index(letter))
 #       modList.append((letters.index(letter)+1) % 4)
  #      if not letter in letters:
#	    return False

    # letters = the dice rolled
    for index, value in enumerate(letters):
        for letter in w:
            if value == letter:
	        #print("The index= ",index, "letter= ",letter)
                #print("Letters index= ",letters.index(letter), "letter= ", letter)
                posList.append(index)
                modList.append((index+1) % 4) 
            if not letter in letters:
                return False
    
    """
    #i = 0
    word = []
    wordIndex = []
    wordCol = []
    size = len(w)
    next_ = 0
    previous = 0
    duplicate = False
    finalWord = []
    finalIndex = []
    finalCol = []
    prevLetter = None 
    # for when mod col = 0
    tempPos = 4
    # for each letter in the word we are checking
    for index, letter in enumerate(w):
        #if duplicate and finalWord and (letter != finalWord[-1]):
        if duplicate and finalWord:
            #print("duplicates stopped at: ", letter)
            for pos in posList:
                if letter == letters[pos]:
                    #print(letter, "found at ", pos, "word[-1]= ", word[-1])
                    if (((pos+1) % 4) ==  (1 - (wordCol[-1]))) or (((pos+1) % 4) == (1 + (wordCol[-1]))) or (((pos+1) % 4) == wordCol[-1] ):
                        #print("pos - wordindex = ", pos, " - ", wordIndex[-1], " = ", abs(pos - (wordIndex[-1])))
                        if ((pos+1) % 4) == 0:
                            if (tempPos ==  (1 - (wordCol[-1]))) or (tempPos == (1 + (wordCol[-1]))) :
                                if (abs(pos - (wordIndex[-1])) <= 5):
                                    finalWord.append(word[-1])
                                    finalIndex.append(wordIndex[-1])
                                    finalCol.append(wordCol[-1])
                        elif (abs(pos - (wordIndex[-1])) <= 5):
                            finalWord.append(word[-1])
                            finalIndex.append(wordIndex[-1])
                            finalCol.append(wordCol[-1])
                        #print("last dup matches col with next letter")
                        #word.append(letter)
                        #wordCol.append(pos)
                    
            duplicate = False
        # see if it matches any positions in boggle list 
        for pos in posList:
            if letter == letters[pos] and prevLetter != letter:
                # is duplicate
                if word and (word[-1] == letters[pos]):
                    duplicate = True
                
                if wordIndex and (wordIndex[-1] != pos):
                    word.append(letter)
                    wordIndex.append(pos)
                    wordCol.append((pos+1) % 4)

                if not word:
                    word.append(letter)
                    wordIndex.append(pos)
                    wordCol.append((pos+1) % 4)

                if not duplicate :
                    if not finalWord:
                        finalWord.append(letter)
                        finalIndex.append(pos)
                        finalCol.append((pos+1) % 4) 
                    #print("final[-1]= ", finalWord[-1], "fcol= ",finalCol[-1], "word[-1]= ", word[-1], "wCol= ", wordCol[-1])
                    elif ((finalCol[-1]) ==  (1 - (wordCol[-1]))) or ((finalCol[-1]) == (1 + (wordCol[-1]))) or finalCol[-1] == wordCol[-1]:
                        #print("inside elif")
                        #finalWord.append(letter)
                        #finalIndex.append(pos)
                        #finalCol.append((pos+1) % 4)
                        if ((pos+1) % 4) == 0:
                            if (tempPos ==  (1 - (finalCol[-1]))) or (((pos+1) % 4) == (1 + (finalCol[-1]))) :
                                if (abs(pos - (finalIndex[-1])) <= 5):
                                    finalWord.append(letter)
                                    finalIndex.append(pos)
                                    finalCol.append((pos+1) % 4)
                        elif (abs(pos - (finalIndex[-1])) <= 5):
                            finalWord.append(letter)
                            finalIndex.append(pos)
                            finalCol.append((pos+1) % 4)

        #if duplicate and finalWord and (letter != finalWord[-1]):
        if duplicate and finalWord:
            #print("duplicates stopped at: ", letter)
            for pos in posList:
                if letter == letters[pos]:
                    #print(letter, "found at ", pos, "word[-1]= ", word[-1])
                    if (((pos+1) % 4) ==  (1 - (wordCol[-1]))) or (((pos+1) % 4) == (1 + (wordCol[-1]))) or (((pos+1) % 4) == wordCol[-1] ):
                        #print("pos - wordindex = ", pos, " - ", wordIndex[-1], " = ", abs(pos - (wordIndex[-1])))
                        if ((pos+1) % 4) == 0:
                            if (tempPos ==  (1 - (wordCol[-1]))) or (tempPos == (1 + (wordCol[-1]))) :
                                if (abs(pos - (wordIndex[-1])) <= 5):
                                    finalWord.append(word[-1])
                                    finalIndex.append(wordIndex[-1])
                                    finalCol.append(wordCol[-1])
                        elif (abs(pos - (wordIndex[-1])) <= 5):
                            finalWord.append(word[-1])
                            finalIndex.append(wordIndex[-1])
                            finalCol.append(wordCol[-1])
                        #print("last dup matches col with next letter")
                        #word.append(letter)
                        #wordCol.append(pos)
                    
            duplicate = False         
        #print("the word= ", word)
        #print("the index=", wordIndex)    
        print("the finalword= ", finalWord)
        print("the finalindex= ", finalIndex)
        prevLetter = letter        
                
    end = len(word)
    offset = 0
    
   
    #for letter in w:
    #    for index, val in enumerate(word):
    #        if ((index + 1) < (end - 1)) and (word[index] == word[index + 1]):
                
                
    
    for index, letter in enumerate(word):
        # check if next letter is duplicate
        if (index < (end - 1)) and (letter == word[ index + 1 ]):
            #print("multi letters", letter)
            # offset = duplicate counter, while loop grabs all
            offset = 1
            #while (word[ index + offset + 1] < (end - 1)) and (word[ index + offset + 1] == letter):
            while (word[ index + offset + 1] < (end)) and (word[ index + offset + 1] == letter):
                offset += 1
            # duplicate found
            if offset > 0: 
                if (offset + 1) < (end):
                    #print("NEXT COL AFTER DUPLIC: ",wordCol[ offset + 1 ], "col minus = ",(1 - (wordCol[ offset ])) )
                    if wordCol[ offset + 1 ] == ((1 + (wordCol[ offset ])) or (1 - (wordCol[ offset ]))):
                        print("columns near each other")
                        # if first letter is duplicate
                        if not finalWord:
                            print("adding the duplicate located at: ", wordIndex[offset])
                            finalWord.append( word[offset] )
                            finalCol.append( wordCol[offset] )
                            finalIndex.append( wordIndex[offset])
                        if finalWord:
                            if finalCol[-1] == ((1 + (wordCol[ offset ])) or (1 - (wordCol[ offset ]))):
                                print("adding the duplicate located at: ", wordIndex[offset])
                                finalWord.append( word[offset] )
                                finalCol.append( wordCol[offset] )
                                finalIndex.append( wordIndex[offset])
        else:
            finalWord.append(letter)

    print("final word: ", finalWord)
    
    print("WORD EXISTS: ", word, "theindex= ", wordIndex)
    #print(posList, modList)
    """ 
    return True

def isValid(w, words, letters):
    # setup the dictionary
    d = enchant.Dict("en_US")

    letterFlag = True
    for letter in w:
        if w.count(letter) > letters.count(letter):
            letterFlag = False
    
    #1 not been scored
    if w in words: 
        print("The word", w, "has already been used.")

    #2 at least 3 letters
    elif not len(w) > 2:
        print("The word", w, "is too short.")

    #3 must be word in english language
    elif not d.check(w): 
        print("The word", w, "... not a word.")

    #4 be present in boggle display
    elif not inGame(w, letters):
        print("The word", w, " is not in boggle display.")    
    #5 letters only used once
    elif not letterFlag:
        print("The word", w, " cannot use same letter more than once.")
    # criteria passed. add points to total
    else:
        if len(w) < 5:
            print("The word", w, "is worth", points(w), "point.")
	    return points(w)
        else:
            print("The word", w, "is worth", points(w), "points.")
	    return points(w)

    return 0

# setup the dice
die1 =  ["A","E","A","N","E","G"]
die2 =  ['A','H','S','P','C','O']
die3 =  ['A','S','P','F','F','K']
die4 =  ['O','B','J','O','A','B']
die5 =  ['I','O','T','M','U','C']
die6 =  ['R','Y','V','D','E','L']
die7 =  ['L','R','E','I','X','D']
die8 =  ['E','I','U','N','E','S']
die9 =  ['W','N','G','E','E','H']
die10 = ['L','N','H','N','R','Z']
die11 = ['T','S','T','I','Y','D']
die12 = ['O','W','T','O','A','T']
die13 = ['E','R','T','T','Y','L']
die14 = ['T','O','E','S','S','I']
die15 = ['T','E','R','W','H','V']
die16 = ['N','U','I','H','M','QU']

# set array. roll the dice
dice = []
dice.append(random.choice(die1))
dice.append(random.choice(die2))
dice.append(random.choice(die3))
dice.append(random.choice(die4))
dice.append(random.choice(die5))
dice.append(random.choice(die6))
dice.append(random.choice(die7))
dice.append(random.choice(die8))
dice.append(random.choice(die9))
dice.append(random.choice(die10))
dice.append(random.choice(die11))
dice.append(random.choice(die12))
dice.append(random.choice(die13))
dice.append(random.choice(die14))
dice.append(random.choice(die15))
dice.append(random.choice(die16))

# shuffle the dice
random.shuffle(dice)

i = 1
for die in dice:
    if (i % 4 == 0):
        print('[', die,'] ',sep = '',end = '')
        print("\n")
    else:
	print('[', die,'] ',sep = '',end = '')
    i += 1

# declare variables
end = 'X'
guess = []
usedWords = []
totalPoints = 0

# read in values until 'X'
print("\nStart Typing your words! (press enter after each word and enter #'X' when done): ")
for val in iter(raw_input, end):
    guess.append(val.upper())

# total points and check words
for isWord in guess:
    totalPoints += isValid(isWord, usedWords, dice)
    usedWords.append(isWord)

# output total score
if totalPoints == 1:
    print("Your total score is", totalPoints, "point!")
else:
    print("Your total score is", totalPoints, "points!")
