#!/usr/bin/python


def main():
    func(2)
    func(3)
    func(4)
    func()


def func(a=5):
    for i in range(a,10):
        print(i, end=' ')
    print()

if __name__ == "__main__": main()