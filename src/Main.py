# coding=utf-8

from Initializer import getText
from EMStep import EMIter
from Score import calcScore, calcFreq

text = getText('chapter1.txt')
dictionary = EMIter(5, 5, text)
# final_dictionary = calcScore(text, dictionary)
temp = []
temp.append(dictionary)
prep_all_dict = calcFreq(temp)
final_dictionary = prep_all_dict[0]

final_dictionary = sorted(final_dictionary.items(), key=lambda d: d[1], reverse=True)
for item in final_dictionary:
    if len(item[0]) > 1:
        print item[0], ':', item[1]
