#!/usr/bin/python


def main():
    s = 'This is a string'
    for c in s:
        if c == 's':continue  #ELIMINA OS 'S'
        print(c, end='')

        
if __name__ == "__main__":main()