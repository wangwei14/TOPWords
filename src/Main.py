# coding=utf-8

from Initializer import getText
from EMStep import EMIter
from Score import calcScore, calcFreq
import math

tauL = 5
tauF = 5

text = getText('chapter1.txt')
dictionary = EMIter(tauL, tauF, text)
# final_dictionary = calcScore(text, dictionary)
temp = []
temp.append(dictionary)
prep_all_dict = calcFreq(temp)
final_dictionary = prep_all_dict[0]

# final_dictionary = sorted(final_dictionary.items(), key=lambda d: d[1], reverse=True)
# for item in final_dictionary:
#     if len(item[0]) > 1:
#         print item[0], ':', item[1]


def generator(sentence, dictionary, sent_dict):
	length = len(sentence)
	if length == 1:
		return math.log(dictionary[sentence]), [sentence]
	if sentence in sent_dict:
		return sent_dict[sentence]
	tempMax = -500
	words = []
	for i in range(0, tauL):
		if length > i:
			tempWord = sentence[0:i]
			if tempWord in dictionary.keys():
				tempTheta, _words = generator(sentence[i:length], dictionary, sent_dict)
				tempTheta += math.log(dictionary[tempWord])
				if tempTheta > tempMax:
					tempMax = tempTheta
					words = [tempWord]
					words = words + _words
		else:
			break
	theta = tempMax
	sent_dict[sentence] = [theta, words]

	return theta, words

def splitor(text, dictionary):
	ans = []
	for sentence in text:
		sent_dict = {}
		_, words = generator(sentence, dictionary, sent_dict)
		ans = ans + words

	return ans

# theta, words = generator(text[48], final_dictionary)
# for item in words:
# 	print item
dddd = splitor(text, final_dictionary)
# for item in dddd:
# 	print item
