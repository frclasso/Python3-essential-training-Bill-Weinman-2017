#!/usr/bin/python

import re


def main():

    fh = open('raven.txt')
    pattern = re.compile('(Len|Neverm)ore', re.IGNORECASE)
    for line in fh:
        if re.search(pattern, line):
            print(pattern.sub('###',line), end='')


if __name__ == "__main__":main()