# Projet de TAL
## Analyse avec Stanford
### I - Evaluation de l'analyse morpho-syntaxique
1. Conversion d'un fichier analysé avec des labels LIMA en fichier avec des labels Stanford, puis en fichier avec des tags universels.
```
./convertLimaToStanford.py ../data/pos_reference.txt.lima > ../data/pos_reference.txt.ptb
./convertStanfordToUniv.py ../data/pos_reference.txt.ptb > ../data/pos_reference.txt.univ
```
2. Transformation du fichier avec labels universels en fichier .txt simple.
```
./extractText.py ../data/pos_reference.txt.univ > ../data/pos_test.txt
```
3. Analyse du fichier avec Stanford
```
./stanford-postagger.sh models/english-left3words-distsim.tagger ../../data/pos_test.txt > ../../data/pos_test.txt.pos.stanford.tmp
```
Formattage
```
./format.py ../data/pos_test.txt.pos.stanford.tmp > ../data/pos_test.txt.pos.stanford
```

4. Conversion des résultats en labels universels.
```
./convertFormattedToUniv.py -ptb ../data/pos_test.txt.pos.stanford > ../data/pos_test.txt.pos.stanford.univ
```

5. Evaluation du résultat
```
python evaluate.py ../data/pos_test.txt.pos.stanford.univ ../data/pos_reference.txt.univ
```
Résultat :
```
Word precision: 0.0096287472702
Word recall: 0.00891134588884
Tag precision: 0.0096287472702
Tag recall: 0.00891134588884
Word F-measure: 0.00925616680185
Tag F-measure: 0.00925616680185
```

### II - Evaluation de la reconnaissance d’entités nommées
1. Extraction du texte original
```
./extractText.py ../data/ne_reference.txt.conll > ../data/ne_test.txt
```
2. Analyse des entitées nommées avec Stanfort
```
java -mx600m -cp stanford-ner.jar:lib/* edu.stanford.nlp.ie.crf.CRFClassifier -loadClassifier classifiers/english.all.3class.distsim.crf.ser.gz -textFile ../../data/ne_test.txt > ../../data/ne_test.txt.ne.stanford.tmp
```
Formattage :
```
./format.py ../data/ne_test.txt.ne.stanford.tmp > ../data/ne_test.txt.ne.stanford
```

3. Conversion en labels CoNLL-2003
```
./convertStanfordToConll.py ../data/ne_test.txt.ne.stanford > ../data/ne_test.txt.ne.stanford.conll
```

4. Evaluation du résultat
```
python evaluate.py ../data/ne_test.txt.ne.stanford.conll ../data/ne_reference.txt.conll
```
Résultat :
```
Word precision: 0.0143027413588
Word recall: 0.0143027413588
Tag precision: 0.0143027413588
Tag recall: 0.0143027413588
Word F-measure: 0.0143027413588
Tag F-measure: 0.0143027413588
```
