#!/usr/bin/python


def main():
    for n in testFunc(): print(n, end=',')


def testFunc():
    return range(25)


if __name__ == "__main__":main()