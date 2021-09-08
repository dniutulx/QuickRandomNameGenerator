
import random

def addLetters(array: list, letter, count: int) -> list:
    for x in range(0, count):
        array.append(letter)
    return array

def nameme(length: int, letterBag: list) -> str:
    name = ''
    cap = True
    for x in range(0, length):
        here = random.randrange(len(letterBag))
        letter = letterBag[here]
        if cap: letter = letter.upper()
        if letter.isalpha(): cap = False
        else: cap = True
        name += letter
        del letterBag[here]
    del letterBag
    return name
    
    
#   EDIT THIS SECTION

# Each line add a number of each "tile" to the bag.
# To change language or tone, update the numbers for each letter, or add your own characters.
# letters = addLetters(letters, '{your character here}', {how many to add}')

letters = []
letters = addLetters(letters, 'a', 9)
letters = addLetters(letters, 'b', 2)
letters = addLetters(letters, 'c', 2)
letters = addLetters(letters, 'd', 5)
letters = addLetters(letters, 'e', 13)
letters = addLetters(letters, 'f', 2)
letters = addLetters(letters, 'g', 3)
letters = addLetters(letters, 'h', 4)
letters = addLetters(letters, 'i', 8)
letters = addLetters(letters, 'j', 1)
letters = addLetters(letters, 'k', 1)
letters = addLetters(letters, 'l', 4)
letters = addLetters(letters, 'm', 2)
letters = addLetters(letters, 'n', 5)
letters = addLetters(letters, 'o', 8)
letters = addLetters(letters, 'p', 2)
letters = addLetters(letters, 'q', 1)
letters = addLetters(letters, 'r', 6)
letters = addLetters(letters, 's', 5)
letters = addLetters(letters, 't', 7)
letters = addLetters(letters, 'u', 4)
letters = addLetters(letters, 'v', 2)
letters = addLetters(letters, 'w', 2)
letters = addLetters(letters, 'x', 1)
letters = addLetters(letters, 'y', 2)
letters = addLetters(letters, 'z', 1)
letters = addLetters(letters, '\'', 2)

#   don't change below here


#minLength = int(input(f'how many letters minimum? (1-{str(len(letters))}) '))
#maxLength = int(input(f'how many letters minimum? ({minLength}-{str(len(letters))}) '))

#second google hit for online python doesn't yet support fstrings
minLength = int(input('how many letters minimum? (1-'+ str(len(letters))+') '))
maxLength = int(input('how many letters minimum? ('+ str(minLength)+'-'+str(len(letters))+') '))

more = 'ya'

while more != 'no':
    length = random.randrange(minLength, maxLength+1)
    more = input(nameme(length, letters.copy()) + '    another?' ) 



