#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

x = 42
y = 73

if x < y:
    print('x is less than y')
else:
    print('y is less than x')

def compareVals(a, b):
  if a < b:
    print(f'{a} is less than {b}')
  elif a is b:
    print('values are equal')
  else:
    print(f'{b} is less than {a}')

compareVals(402, 402)