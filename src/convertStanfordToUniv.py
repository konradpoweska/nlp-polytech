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
  for token in re.split('\n', inStr):
    if('\t' not in token):
        outTokens.append('\n')
        continue
    pair = token.split('\t')
    if pair[1] not in replaceMap:
      replaceMap[pair[1]]="None"
    pair[1] = replaceMap[pair[1]]
    outTokens.append('\t'.join(pair)+"\n")

  return ''.join(outTokens)


if __name__ == "__main__":
  with open('POSTags_PTB_Universal_Linux.txt', 'r') as f:
    tokenMap = genMapFromFile(f)

  # print(tokenMap)

  with open(sys.argv[1]) as f:
    out = replaceLabels(f.read(), tokenMap)

  print(out)
