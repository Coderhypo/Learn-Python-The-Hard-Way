#!/usr/bin/env python
# coding=utf-8

def loop(num):
    i = 0
    numbers = []
    for i in range(0, num):
        print "At the top i is %d" % i
        numbers.append(i)

        i = i + 1
        print "numbers now:", numbers
        print "At the bottom i is %d" % i

    return numbers

numbers = loop(int(raw_input()))

print "The numbers:"

for num in numbers:
    print num

