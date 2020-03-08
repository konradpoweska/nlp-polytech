#!/usr/bin/python3
import sys

def genMapFromFile(file):
  replaceMap = {}
  for line in file:
    pair = [ x for x in line[:-1].split(' ') if len(x)>0 ]
    if(len(pair) > 1):
      replaceMap[pair[0]] = pair[1]
  return replaceMap


def replaceLabels(inStr, replaceMap):
  outTokens = []

  import re
  for token in re.split(' |\n', inStr):
    if('_' not in token):
      continue
    pair = token.split('_')
    # print(pair[1], pair[1] in replaceMap)
    if pair[1] not in replaceMap:
      print("Error.")
    pair[1] = replaceMap[pair[1]]
    outTokens.append('_'.join(pair))

  return ' '.join(outTokens)


if __name__ == "__main__":
  with open('POSTags_PTB_Universal_Linux.txt', 'r') as f:
    tokenMap = genMapFromFile(f)

  # print(tokenMap)

  with open(sys.argv[1]) as f:
    out = replaceLabels(f.read(), tokenMap)

  print(out)



