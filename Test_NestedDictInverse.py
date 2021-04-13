# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 22:10:57 2021

@author: Tony
"""

import unittest
import NestedDictInverse

class Test_NestedDictInverse(unittest.TestCase):

    def test_str(self):
        input_value = {'hired': {'be': {'to': {'deserve': 'I'}}}}
        result = NestedDictInverse.hlper_fnc(input_value);
        print(result)
        self.assertEqual({'I': {'deserve': {'to': {'be': 'hired'}}}}, result);

    def test_int(self):
        input_value = {1: {10: {15: {20: 25}}}}
        result = NestedDictInverse.hlper_fnc(input_value);
        print(result)
        self.assertEqual({25: {20: {15: {10: 1}}}}, result);
        
        
    def test_randomtype(self):
        input_value = {'a': {10: {15.6: {(): 'd'}}}}
        result = NestedDictInverse.hlper_fnc(input_value);
        print(result)
        self.assertEqual({'d': {(): {15.6: {10: 'a'}}}}, result);

        

if __name__ == '__main__':
    unittest.main()