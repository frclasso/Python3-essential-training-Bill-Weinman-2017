#!/usr/bin/python


def main():
    a, b = 0,1
    while b < 150:
        print(b, end=" - ")
        a,b =b, a + b

if __name__ == "__main__":main()