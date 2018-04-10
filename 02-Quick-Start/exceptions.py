#!/usr/bin/python

#TRATAMENTO DE EXCESSOES USANDO 'TRY e EXCEPT'

try:
    fh = open('xlines.txt')
    for line in fh.readlines():
        print(line, end="")
except IOError as e:
    print("\nSomething wrong happened ({})".format(e))

print(" \nAfter badness!")