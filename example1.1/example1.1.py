#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 17:28:30 2024

@author: sandro
"""

print('-'*28,'CODE OUTPUT','-'*29)

inputs = {
        'a': 0.00007,
        'b': 1.64e-4,
        'c': 10,
        'd': complex(3,4),
        'e':'time'}

for key, value in inputs.items():
    print(f'\nVariable {key} = {value} belongs to type:',type(value))