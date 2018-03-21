#!/usr/bin/python


def main():
    choices = dict(
        one='first',
        two='second',
        three='third',
        four='fourth',
        five='fifth'
    )

    v = 'seven'
    print(choices.get(v, 'wrong choice!'))  # 'wrong choice is a default value

if __name__ == "__main__":main()