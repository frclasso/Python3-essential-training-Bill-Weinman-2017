#!/usr/bin/python


def main():
    fh = open('/home/fabio/Desktop/estudo_ti/Python/'
              'Python3-essential-training-Bill-Weinman/'
              '02-Quick-Start/lines.txt')
    for index, line in enumerate(fh.readlines()):
        print(index, line, end='')

if __name__ == "__main__":main()