#!/usr/bin/python


def main():
    testFunc(1,2,3,41,42,43)


def testFunc(this, that, other, *args): #*args = List of optional arguments
    print(this, that, other)
    for n in args:print(n, end=',')


if __name__ == "__main__":main()