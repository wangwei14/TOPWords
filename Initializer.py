# coding=utf-8

import re
from zhon.hanzi import punctuation


# input:   fileName: Source file name
#
# output:  all_text: List of all the sentences from the file
def getText(fileName):
    all_text = ""
    file_object = open(fileName, 'r')
    try:
        all_text += file_object.read()
    finally:
        file_object.close()
    all_text = re.sub(ur"[%s]+" % punctuation, ' ', all_text.decode("utf-8"))
    all_text = all_text.split()
    # for item in all_text:
    #     print item

    return all_text


# input:  tauL: Max length of a word, constant assigned by user
#         tauF: Min appearing times of a word, constant assigned by user
#         all_text: The text need to be processed
#
# output: all_dict: The overcomplete dictionary
def getOverDictionary(tauL, tauF, all_text):
    all_dict = {}
    for item in all_text:
        for i in range(1, tauL+1):
            for j in range(0, len(item)+1-i):
                temp = item[j:j+i]
                if temp in all_dict:
                    all_dict[temp] += 1
                else:
                    all_dict[temp] = 1
    for key, value in all_dict.items():
        if value < tauF and len(key) > 1:
            del all_dict[key]
    # for key, value in all_dict.items():
    #     print key, ':', value

    return all_dict
