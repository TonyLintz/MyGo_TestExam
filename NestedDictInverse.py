# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 22:10:18 2021

@author: Tony
"""

def flat_nested_dict(input_dict, collect_list):
    if type(input_dict) != dict:
        return [collect_list + [input_dict]]
    temp = []
    for key in input_dict:
        temp.extend(flat_nested_dict(input_dict[key], collect_list + [key]))
    return temp
    


def hlper_fnc(test_dict):
    all_nesteddict_to_flattenlist = flat_nested_dict(test_dict, [])
    inv_dict = {}
    for flattenlist in all_nesteddict_to_flattenlist:
        tmp_dict = inv_dict
        for ele in range(len(flattenlist)):
            if ele == (len(flattenlist)-1):
                break
            if (flattenlist[::-1][ele] not in tmp_dict) :
                if (ele == (len(flattenlist)-2)):
                    tmp_dict[flattenlist[::-1][ele]] = flattenlist[::-1][ele+1]
                else:
                    tmp_dict[flattenlist[::-1][ele]] = {}  
            tmp_dict = tmp_dict[flattenlist[::-1][ele]]
    return inv_dict



