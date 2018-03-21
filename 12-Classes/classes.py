#!/usr/bin/python


class Duck:
    def quack(self):
        print('Quaaaaaaak!')

    def walk(self):
        print("Walk like a Duck!")


def main():
    donald = Duck()
    donald.quack()
    donald.walk()


if __name__ == "__main__":main()