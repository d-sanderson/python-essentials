#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

class Duck:
    sound = 'Talks like a duck'
    walking = 'Walks  like a duck.'
    def quack(self):
      print(self.sound)
    def walk(self):
      print(self.walking)

class Donald(Duck):
    sound = 'Give me your stuff'
    def rob(self):
      print(self.sound)
    def walk(self):
      print('I am walking')

def main():
    donald = Duck()
    donald.quack()
    donald.walk()
    ronald = Donald()
    ronald.rob()
    ronald.walk()

if __name__ == '__main__': main()
