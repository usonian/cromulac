#!/usr/bin/python

import random
import sys
import re
import math

def buildWord(base, wordTable, accuracy):
  stub = base[-3:]
  #Find the most likely next letter and add it
  if stub in wordTable.keys():

    nextKeys = wordTable[stub].keys()
    #http://desk.stinkpot.org:8080/tricks/index.php/2006/10/find-the-key-for-the-minimum-or-maximum-value-in-a-python-dictionary/
    nextKeys.sort(cmp=lambda a,b: cmp(table[stub][a],table[stub][b]))

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
#Keep a separate list of starting stubs for simplicity
start = []

for word in sys.stdin:
 #word = word.lower()

  for i in range(0, len(word) - 3):
    stub = word[i:i+3]
    
    if (i == 0):
      try:
        startExists = start.index(stub)
      except:
        start.append(stub)
    
    if (i <= (len(word) - 3)):
      character = word[i+3:i+4]
    else:
      character = "\n"
    
    table.setdefault(stub, {})
    
    if table[stub].has_key(character):
      table[stub][character] = table[stub][character] + 1
    else:
      table[stub][character] = 1

minlength = 5
wordsplease = 100
accuracy = float(85)

words = []
while len(words) < wordsplease:
  #Pick a random starting stub
  stub = random.choice(start)
  word = buildWord(stub, table, accuracy)
  if (len(word) >= minlength):
    words.append(word)

for word in words:
  print word.rstrip(' \n')