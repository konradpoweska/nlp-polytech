#!/usr/bin/python3
import sys
import nltk
from nltk.tokenize import word_tokenize

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as inFile:
        tokens = nltk.word_tokenize(inFile.read())

    posPairs = nltk.pos_tag(tokens)

    for p in posPairs:
        print("%s\t%s" % p)
