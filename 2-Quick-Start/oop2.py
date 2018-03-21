#!/usr/bin/python

#class implementation


class AnimalActions:
    def quack(self): return self.strings['quack']

    def feathers(self): return self.strings['feathers']

    def bark(self): return self.strings['bark']

    def fur(self): return self.strings['fur']


class Duck(AnimalActions):
    strings = dict(
        quack="Quaaaaaack!",
        feathers="The duck has gray and white feathers.",
        bark="The Duck cannot bark.",
        fur="The Duck has no fur."
    )


class Person(AnimalActions):
    strings = dict(
        quack="The person imitates a duck.",
        feathers="The person takes a feathers from the ground and shows it!",
        bark="The person says woof!",
        fur="The person puts on a fur coat."
    )


class Dog(AnimalActions):
    strings = dict(
        quack="The dog cannot quack.",
        feathers="The has no feathers.",
        bark="Arf!",
        fur="The Dog has white fur with black spots."
    )


def in_the_doghouse(dog):
    print(dog.bark())
    print(dog.fur())


def in_the_forest(duck):
    print(duck.quack())
    print(duck.feathers())


def main():
    donald = Duck()
    john = Person()
    fido = Dog()

    print("**In the Forest:")
    for o in (donald, john, fido):
        in_the_forest(o)

    print("***************")
    print("**In the doghouse:")
    for o in (donald, john, fido):
        in_the_doghouse(o)


if __name__ == "__main__":main()