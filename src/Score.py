# coding=utf-8

import math
import copy
from EMStep import DPLeft


# Calculate P(T | D, theta)
def calcProb(all_text, over_dict, local_word):
    local_dict = copy.copy(over_dict)
    if local_word in local_dict:
        local_dict[local_word] = 0.0

    likelihood = 0.0
    for sentence in all_text:
        leftS = DPLeft(sentence, local_dict)
        ALPHA = leftS[len(sentence) + 1]
        likelihood += ALPHA
    likelihood /= len(all_text)

    return likelihood


# input:  all_text: The text need to be processed
#         all_dict: The overcomplete dictionary after the EM iteration step
#
# output: score_dict: Significance scores of words longer than one in the dictionary
def calcScore(all_text, over_dict):
    all_score = calcProb(all_text, over_dict, '')
    score_dict = {}

    for key in over_dict:
        if len(key) > 1:
            temp_score = calcProb(all_text, over_dict, key)
            score_dict[key] = math.log(all_score / temp_score)

    return score_dict


# input:  all_dict: All dictionaries from K target texts
#
# output: freq_all_dict: Relative frequency of the word to one specific target text
def calcFreq(all_dict):
    if len(all_dict) == 1:
        return all_dict
    else:
        sum_dict = {}
        for l_dict in all_dict:
            for key, value in l_dict.items():
                if key in sum_dict:
                    sum_dict[key] += value
                else:
                    sum_dict[key] = value

        freq_all_dict = []
        for i in range(len(all_dict)):
            for key, value in all_dict[i]:
                freq_all_dict[i][key] = value / sum_dict[key]

    return freq_all_dict
