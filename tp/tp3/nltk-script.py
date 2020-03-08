#!/usr/bin/python3
import sys
import re

import nltk
from nltk.tokenize import word_tokenize
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')

# Writes tab-separated pairs in separate lines
def writeStandard(pairs, outFile):
  for p in pairs:
    outFile.write("%s\t%s\n" % p)

### Partie 1

## Q1.1
with open('../wsj_0010_sample.txt', 'r') as inFile:
  tokens = word_tokenize(inFile.read())

posPairs = nltk.pos_tag(tokens)

## Q1.2
with open('../wsj_0010_sample.pos.ref', 'r') as refFile:
  ref = [ tuple(re.findall('\S+', line)) for line in refFile ]

if len(posPairs) != len(ref):
  print("Error: result and ref is not the same length")
  exit

for i in range(len(posPairs)):
  token,tag = posPairs[i]
  refToken,_,*_ = ref[i]
  if token != refToken:
    print("Changing token from %s to %s." % (token, refToken))
    posPairs[i] = (refToken,tag)


with open('wsj_0010_sample.txt.pos.nltk', 'w') as outFile:
  writeStandard(posPairs, outFile)

## Q1.3
tagsMap = {}
with open('../POSTags_PTB_Universal_Linux.txt', 'r') as file:
  for line in file:
    words = re.findall('\S+', line)
    tagsMap[words[0]] = words[1]

# replaces second member of pair according to map
def replaceTags(pairs, tagsMap):
  return [ (p[0], tagsMap[p[1]] or print("Error: tag %s not found in map." % p[1])) for p in pairs ]

refUniv = replaceTags(ref, tagsMap)
posPairsUniv = replaceTags(posPairs, tagsMap)

with open('wsj_0010_sample.txt.pos.univ.nltk', 'w') as f:
  writeStandard(posPairsUniv, f)

with open('wsj_0010_sample.txt.pos.univ.ref', 'w') as f:
  writeStandard(refUniv, f)


### Partie 2

# Q1.1
# grammar = "Compound: {<DT>?<JJ1>*<NN>}"
# chunker = nltk.RegexpParser(grammar)
# output = chunker.parse(posPairs)

# Q1.2

# Adjectif-Nom
# Nom-Nom
# Adjectif-Nom-Nom
# Adjectif-Adjectif-Nom

patterns = """
  P1: {<JJ.?><NNS?P?>}
  P2: {<NNS?P?>{2}}
  P3: {<JJ.?><NNS?P?>{2}}
  P4: {<JJ.?>{2}<NNS?P?>}
"""
chunker = nltk.RegexpParser(patterns)
output = chunker.parse(posPairs)
# print(output)


### Partie 3
ne_tree = nltk.ne_chunk(posPairs)
iob_tagged = nltk.tree2conlltags(ne_tree)

# print(iob_tagged)
