#!/usr/bin/python

import random
import sys
import re
import math

def buildWord(base, wordTable, accuracy):
  pair = base[-2:]
  #Find the most likely next letter and add it
  if pair in wordTable.keys():

    nextKeys = wordTable[pair].keys()
    #http://desk.stinkpot.org:8080/tricks/index.php/2006/10/find-the-key-for-the-minimum-or-maximum-value-in-a-python-dictionary/
    nextKeys.sort(cmp=lambda a,b: cmp(table[pair][a],table[pair][b]))

    #Chose a random index in the top 80% of those available
    lowerIdx = int(math.floor(len(nextKeys) * (accuracy / 100.0)))
    upperIdx = len(nextKeys)

    idx = random.randint(lowerIdx, upperIdx) - 1

    base += nextKeys[idx]

    newBase = base
    while len(base) < 40:
      newBase = buildWord(base, wordTable, accuracy)
      if (newBase == base):
        break
      else:
        base = newBase

    return newBase
  else:
    return base

nonword = "\n"
w1 = nonword
w2 = nonword

#Generate table
table = {}
#Keep a separate list of starting pairs for simplicity
start = []

for word in sys.stdin:
  word = word.lower()

  for i in range(0, len(word) - 2):
    pair = word[i:i+2]
    if i == 0:
      start.append(pair)
    if (i == len(word) - 2):
      character = word[i+1:i+2]
    else:
      character = word[i+2:i+3]

    table.setdefault(pair, {})
    
    if table[pair].has_key(character):
      table[pair][character] = table[pair][character] + 1
    else:
      table[pair][character] = 1

minlength = 5
wordsplease = 10
accuracy = float(90)

words = []
while len(words) < wordsplease:
  #Pick a random starting pair
  pair = random.choice(start)
  word = buildWord(pair, table, accuracy)
  if (len(word) >= minlength):
    words.append(word)

for word in words:
  print word