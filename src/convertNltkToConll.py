#!/usr/bin/python3
import sys
import re

tagMap = {
  'FACILITY': 'MISC',
  'ORGANIZATION': 'ORG',
  'PERSON': 'PER',
  'GPE': 'LOC',
  'GSP': 'LOC',
  'LOCATION': 'LOC',
  'O': 'O'
}

if __name__ == "__main__":
  with open(sys.argv[1]) as file:
    for line in file:
      nePair = re.findall('\S+', line)

      if nePair[1] != 'O':
        iob = nePair[1][0]
        tag = tagMap[nePair[1][2:]]
        nePair[1] = iob+'-'+tag

      print('\t'.join(nePair))
