#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# if True:
#     print('if true')
# elif False:
#     print('elif true')
# else:
#     print('neither true')

def isPrime(n):
  if n is 1:
      print(False)
  elif n % 2:
      print(False)
  else:
      print(True)

isPrime(40)
isPrime(1)