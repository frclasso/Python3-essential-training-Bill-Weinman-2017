#!/usr/bin/python


def main():
    testFunc(5,6,7,8,9,10, one=1, two=2, three=3, four=4)


def testFunc(this, that, other, *args, **kwargs): #kwargs = key words arguments
    print()
    print("This is a test function",
          kwargs['one'], kwargs['two'], kwargs['three'], kwargs['four'],
          this, that, other, args,
          )
    print()
    print('kwargs in a fo loop')
    for k in kwargs:print(k, kwargs[k])


if __name__=="__main__":main()