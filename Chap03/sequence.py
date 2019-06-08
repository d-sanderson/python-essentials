#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

x = list(range(6))
for i in x:
    print('i is {}'.format(i))

print(x)

# Dictionary
count = { 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
count['three'] = 50
for k, v in count.items():
   print(f'key is {k}, value is {v}')