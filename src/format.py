#!/usr/bin/python3
import sys

def addNewLines(inStr):
    outTokens = []
    import re
    for sentence in re.split('\n', inStr):
        for token in re.split(' ', sentence):
            pair = re.split('_|/', token)
            outTokens.append('\t'.join(pair)+"\n")
        outTokens.append('\n')
    return ''.join(outTokens)


if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        out=addNewLines(f.read())
    print(out)
