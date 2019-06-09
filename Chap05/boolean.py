#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

a = True
b = True
x = ( 'bear', 'bunny', 'tree', 'sky', 'rain' )
y = 'bear'

if a and b:
    print('expression is true')
else:
    print('expression is false')

print(id(y))
print(id(x[0]))