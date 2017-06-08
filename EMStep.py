# coding=utf-8

import copy
from Initializer import getOverDictionary, getText

# Preparation for constants
THETA_MIN = 1e-8
MAX_ITER = 10
STOP_DIFF = 1e-3


# Re-calculate prob theta and drop small ones
def refreshTheta(dictLocal):
    counter = 0.0
    for item in dictLocal.values():
        counter += item
    for key in dictLocal.keys():
        dictLocal[key] /= counter
        if dictLocal[key] <= THETA_MIN and len(key) > 1:
            del dictLocal[key]

    return dictLocal


# Calculate S_left in the formula
def DPLeft(sentence, over_dict):
    leftS = [0 for i in range(len(sentence)+2)]
    for pos in range(1, len(sentence)+2):
        if pos == 1:
            leftS[pos] = 1
        else:
            if pos == 2:
                leftS[pos] = over_dict[sentence[0]]
            else:
                temp = 0
                for j in range(1, pos):
                    segment = sentence[j-1:pos-1]
                    if segment in over_dict:
                        temp += over_dict[segment] * leftS[j]
                leftS[pos] = temp

    return leftS


# Calculate S_right in the formula
def DPRight(sentence, over_dict):
    rightS = [0 for i in range(len(sentence)+1)]
    for pos in range(len(sentence), 0, -1):
        if pos == len(sentence):
            rightS[pos] = 1
        else:
            if pos == len(sentence)-1:
                rightS[pos] = over_dict[sentence[len(sentence)-1]]
            else:
                temp = 0
                for j in range(len(sentence), pos, -1):
                    segment = sentence[pos:j]
                    if segment in over_dict:
                        temp += over_dict[segment] * rightS[j]
                rightS[pos] = temp

    return rightS


# input:  tauL: Max length of a word, constant assigned by user
#         tauF: Min appearing times of a word, constant assigned by user
#         all_text: The text need to be processed
#
# output: all_dict: The overcomplete dictionary after the EM iteration step
def EMIter(tauL=5, tauF=5, all_text=getText('chapter1.txt')):
    over_dict = getOverDictionary(tauL, tauF, all_text)
    over_dict = refreshTheta(over_dict)
    cache_dict = copy.copy(over_dict)
    run_times = 0
    likelihood = 10
    lastlikelihood = 100
    while run_times < MAX_ITER and abs((likelihood-lastlikelihood)/lastlikelihood) > STOP_DIFF:
        lastlikelihood = likelihood
        likelihood = 0.0
        for sentence in all_text:
            leftS = DPLeft(sentence, over_dict)
            rightS = DPRight(sentence, over_dict)
            ALPHA = leftS[len(sentence)+1]
            likelihood += ALPHA
            for i in range(1, len(sentence)+1):
                for j in range(i, len(sentence)+1):
                    segment = sentence[i-1:j]
                    if segment in over_dict:
                        cache_dict[segment] += leftS[i] * over_dict[segment] * rightS[j] / ALPHA
        likelihood /= len(all_text)
        print likelihood
        run_times += 1
        print run_times
        over_dict = copy.copy(cache_dict)
        over_dict = refreshTheta(over_dict)

    return over_dict


# text = getText('chapter1.txt')
# dictionary = EMIter(5, 5, text)
# dictionary = sorted(dictionary.items(), key=lambda d: d[1], reverse=True)
# for item in dictionary:
#     if len(item[0]) > 1:
#         print item[0], ':', item[1]
