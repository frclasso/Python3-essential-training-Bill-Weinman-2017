#!/usr/bin/python

import sys


def main():
    print("Python version {}.{}.{}".format(*sys.version_info))
    print(sys.platform)
    print()

    #Funcoes do sistema operacional
    import os
    print((os.name))
    print(os.getenv('PATH'))
    print(os.getcwd())
    print(os.urandom(25))
    print()

    #Trabalhando com url's
    import urllib.request
    page = urllib.request.urlopen('https://docs.python.org/3/tutorial/index.html')
    print(page)
    print()
    for line in page: print(str(line, encoding='utf_8'), end='')



if __name__=="__main__":main()