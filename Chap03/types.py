#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/
from decimal import *
#  tuple
x = ('test', 2)
#  list
y = [3, 'four']
#  set
z = {'test' , 3}
print(f'x is {x}')
print(f'x type is {type(x)}')
print(f'y is {y}')
print(f'y type is {type(y)}')
print(f'z is {z}')
print(f'z type is {type(z)}')

#  float
a = .1 + .1 + .1 - .3
print(f'a is {a}')

#  integer
b = 5

#  decimal
c = Decimal(.30)
e = Decimal(1.23)
d = c + e - c + e + e
print(f'd is {d}')
#  boolean
true = True