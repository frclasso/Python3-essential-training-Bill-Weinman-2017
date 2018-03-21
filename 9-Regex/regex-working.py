#!/usr/bin/python

import re


def main():

    fh = open('raven.txt')
    for line in fh:
        if re.search('(Len|Neverm)ore', line): # Busca todas as linhas contendo Lenore ou Nervermore
            print(line, end='')



if __name__ == "__main__":main()