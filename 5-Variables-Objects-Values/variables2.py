#!/usr/bin/python


def main():
    n = 42
    s = "This is the number {} ".format(n) # Python3
    s2 = "This is the number %d " % n  # Python2 - obsoleto
    mystring = '''\
    this is a string
    line after line
    of text and more
    text.
    '''

    print(s)
    print(s2)
    print()
    print(mystring)


if __name__ == "__main__":main()