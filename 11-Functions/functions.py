#!/usr/bin/python


def main():
    testFunc(42)


def testFunc(number, another=None, othermore=45):
    if another is None:
        another =112
    print("This is a test function number:", number,',', another,',', othermore)


if __name__ == "__main__":main()