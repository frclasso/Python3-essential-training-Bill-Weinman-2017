#!/usr/bin/python


def main():

    import random
    print(random.randint(1, 1000))
    print()
    x = list(range(25))
    print(x)
    random.shuffle(x)
    print('Shuffle list', x)
    random.shuffle(x)
    print('Shuffle list', x)
    random.shuffle(x)
    print('Shuffle list', x)


if __name__ == "__main__":main()