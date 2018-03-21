#!/usr/bin/python


def main():
    print("This is the function")
    for i in inclusive_range():
        print(i, end=',')


def inclusive_range(*args):
    numargs = len(args)
    if numargs < 1: raise TypeError('Requires at least one argument')
    elif numargs == 1:
        start = 0
        step =1
        stop = args[0]
    elif numargs == 2:
        (start, stop) = args
        step = 1
    elif numargs == 3:
        (start, stop, step) = args
    else:
        raise TypeError("inclusive _range expected at most 3 amrguments, got {}".format(numargs))
    i =start
    while i <= stop:
        yield i
        i += step


if __name__ == "__main__":main()