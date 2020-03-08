#!/usr/bin/python3
import sys

def genMapFromFile(file):
  replaceMap = {}
  for line in file:
    pair = [ x for x in line[:-1].split(' ') if len(x)>0 ]
    if(len(pair) > 1):
      replaceMap[pair[0]] = pair[1]
  return replaceMap


def replaceLabel(inStr, replaceMap):
    outTokens = []

    import re
    for line in re.split('\n', inStr):
        if('\t' not in line):
            outTokens.append('\n')
            continue
        tuple=line.split("\t")
        if tuple[-1] not in replaceMap:
            print("Error.")
        tuple[-1] = replaceMap[tuple[-1]]
        outTokens.append('\t'.join(tuple)+"\n")
    return ''.join(outTokens)


if __name__ == "__main__":
  with open('POSTags_LIMA_PTB_Linux.txt', 'r') as f:
    tokenMap = genMapFromFile(f)

  #print(tokenMap)

  with open(sys.argv[1]) as f:
    out = replaceLabel(f.read(), tokenMap)

  print(out)
