__author__ = 'Phansiri'

import math



bar = 'this is a string'
foo = 'this'

# print foo in bar
# print bar.find('is')
# print bar[5:]
# print bar.split(' ')
# print bar, foo

# def fib(n):
#     '''Print a Fibonacci series up to n.'''
#     a, b = 0, 1
#     while a < n:
#         print(a, end = ' ')
#         a, b = b, a + b
#     print()
#
# fib(100)


def happy():
    return "Happy"

def new():
    return "New"

def year():
    return "Year!"


# n = 0
# while n < 3:
#     print(happy() + " " + new() + " " + year())
#     n = n + 1

l = []
l = [1, 'two', 3, 4]
l = ['a', ['b', 'c']]
del l[0]

d2 = {'size': 4, 'name': 'bob'}

# print 'size' in d2.keys()

def doesExist():
    if 'size' in d2.keys():
        print 'it is in there'
    else:
        print 'it does not exist!'

# for loop in a for each type way
for i in d2:
    print i
