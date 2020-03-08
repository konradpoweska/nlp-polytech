#!/usr/bin/python3
import sys

def deleteLabels(inStr):
    outTokens = []
    import re
    for token in re.split('\n', inStr):
        if ('\t' not in token):
            outTokens.append("\n")
            continue
        tuple = token.split('\t')
        outTokens.append(' '+tuple[0]+'\n')
    return ''.join(outTokens)


if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        out=deleteLabels(f.read())
    print(out)
