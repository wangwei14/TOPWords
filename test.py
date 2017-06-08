# coding=utf-8

import copy

def ttttt(dict):
    local_dict = copy.copy(dict)
    if '1' in local_dict:
        local_dict['1'] = 0

a = {'1':23, '2':34}
ttttt(a)
print a
