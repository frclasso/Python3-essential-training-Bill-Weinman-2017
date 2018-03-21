#!/usr/bin/python


def main():
    s = 'This is a string'
    for c in s:
        if c == 's':break # INTERROMPE A ITERACAO AO ENCONTRAR O PRIMEIRO 'S'
        print(c, end='')

        
if __name__ == "__main__":main()