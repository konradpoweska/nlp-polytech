# TP1
## I-2.
a.
Tagging des mots:
```
./stanford-postagger.sh models/english-left3words-distsim.tagger ../wsj_0010_sample.txt > ../wsj_0010_sample.txt.pos.stanford
```

b. Comparaison résultats entre stanford et résultat de référence
```
python evaluate.py ../wsj_0010_sample.txt.pos.stanford ../wsj_0010_sentence.pos.ref
```
Résultat :
```
Warning: the reference and the candidate consists of different number of lines!
Word precision: 0.967741935484
Word recall: 0.967741935484
Tag precision: 0.935483870968
Tag recall: 0.935483870968
Word F-measure: 0.967741935484
Tag F-measure: 0.935483870968
```

c. Comparaison résultats entre stanford en universelle et résultat de référence en universelle
Exécution du script convertStanfordToUniv.py sur le fichier de Stanford puis sur celui de référence:
```
./convertStanfordToUniv.py ../wsj_0010_sample.txt.pos.stanford > ../wsj_0010_sample.txt.pos.univ.stanford
```
```
./convertStanfordToUniv.py ../wsj_0010_sentence.pos.ref > ../wsj_0010_sample.txt.pos.univ.ref
```
Comparaison :
```
Word precision: 0.967741935484
Word recall: 0.272727272727
Tag precision: 0.935483870968
Tag recall: 0.263636363636
Word F-measure: 0.425531914894
Tag F-measure: 0.41134751773
```
Les résultats sont sensiblement les mêmes (il devrait y avoir une légère amélioration mais elle est artificielle, car les tags universels sont simplement moins précis que ceux de Stanford).

## II-2.
Typage des mots
```
java -mx600m -cp stanford-ner.jar:lib/* edu.stanford.nlp.ie.crf.CRFClassifier -loadClassifier classifiers/english.all.3class.distsim.crf.ser.gz -textFile ../wsj_0010_sample.txt > ../wsj_0010_sample.txt.ner.stanford
```
Affichage :
```
./tablize.py wsj_0010_sample.txt.ner.stanford
```
