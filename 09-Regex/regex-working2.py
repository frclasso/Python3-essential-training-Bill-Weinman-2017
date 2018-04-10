#!/usr/bin/python

import re


def main():

    fh = open('raven.txt')
    for c, line in enumerate(fh):#numerando as linhas das ocorrencias
        match =re.search('(Len|Neverm)ore', line)
        if match:
            print(c, match.group())


if __name__ == "__main__":main()