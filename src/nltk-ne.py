#!/usr/bin/python3
import sys
import nltk
from nltk.tokenize import word_tokenize

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as inFile:
        tokens = nltk.word_tokenize(inFile.read())

    posPairs = nltk.pos_tag(tokens)

    ne_tree = nltk.ne_chunk(posPairs)
    iob_tagged = nltk.tree2conlltags(ne_tree)

    for token,_,ne in iob_tagged:
        print("%s\t%s" % (token, ne))


