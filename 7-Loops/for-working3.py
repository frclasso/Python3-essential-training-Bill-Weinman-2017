#!/usr/bin/python


def main():
    s = 'This is a string'
    for i, c in enumerate(s):
        if c == 's': print('index {} is an s'.format(i))


if __name__ == "__main__":main()