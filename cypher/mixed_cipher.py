"""Paul Fordham | ptf06c """
#!/user/bin/env python
from __future__ import print_function # print()

import sys    # get command line args
import string # get alphabet

# grab file from commandline arg, open it and read in contents
fName = sys.argv[1]
f = open(fName, 'r')
content = f.read()

# get cipher keyword 
cipher = raw_input("Please enter a keyword for the mixed cipher:")

checkedLetters = set()
uniqueCipher = []
cipherText = []
alphas = list(string.ascii_lowercase)
alphaRemoved = []

# remove duplicate letters from input
for letter in cipher:
    if letter not in checkedLetters:
        uniqueCipher.append(letter)
        checkedLetters.add(letter)
uniqueCipher = ''.join(uniqueCipher)

# get alphabet without cipher letters
for letter in alphas:
    if letter not in uniqueCipher:
        alphaRemoved.append(letter)

# convert list to string and concat 
alphaRemoved = ''.join(alphaRemoved)
cipherText = uniqueCipher + alphaRemoved
            
# assign alphabet
plain = string.ascii_lowercase

print("\nPlaintext:", plain)
print("Ciphertext:", cipherText)

# use the index of the letter from alphabet to find its
# index in cipher alphabet(ciphertext) and append to result
result = []
cipherText = list(cipherText)
for letter in content:
    if letter.isalpha():
        if letter.isupper():
            result.append(cipherText[alphas.index(letter.lower())].upper())
        else:
            result.append(cipherText[alphas.index(letter.lower())])
    else:
        result.append(letter)

result = ''.join(result)
print(result)
f.close()
