# coding=utf-8

from Initializer import getText
from EMStep import EMIter
from Score import calcScore

text = getText('chapter1.txt')
dictionary = EMIter(5, 5, text)
score_dictionary = calcScore(text, dictionary)

score_dictionary = sorted(score_dictionary.items(), key=lambda d: d[1], reverse=True)
for item in score_dictionary:
    if len(item[0]) > 1:
        print item[0], ':', item[1]
