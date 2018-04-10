#!/usr/bin/python


def main():
    x = [1,2,3,4,5]
    x.append(6)
    x.insert(0, 9)
    x.insert(7, 7)
    print(x)

    y = 'string'
    print(type(y), y[2:4])

if __name__ == "__main__":main()