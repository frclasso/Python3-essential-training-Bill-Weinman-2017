#!/usr/bin/python


class Duck:
    def __init__(self, value):
        self._v = value

    def quack(self):
        print('Quaaaaaaak!', self._v)

    def walk(self):
        print("Walk like a Duck!", self._v)


def main():
    donald = Duck(51)
    donald.quack()
    donald.walk()

    frank = Duck(71)
    frank.quack()
    frank.walk()


if __name__ == "__main__":main()