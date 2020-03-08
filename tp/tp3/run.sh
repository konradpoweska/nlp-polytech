#!/bin/sh

python3 ./nltk-script.py
echo

echo "// Results for wsj_0010_sample.txt.pos.nltk"
python ../../src/evaluate.py wsj_0010_sample.txt.pos.nltk ../wsj_0010_sample.pos.ref
echo

echo "// Results for wsj_0010_sample.txt.pos.univ.nltk"
python ../../src/evaluate.py wsj_0010_sample.txt.pos.univ.nltk wsj_0010_sample.txt.pos.univ.ref
