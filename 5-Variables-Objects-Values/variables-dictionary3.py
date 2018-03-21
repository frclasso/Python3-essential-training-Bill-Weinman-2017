#!/usr/bin/python


def main():
    d = dict(
        one=1, two=2, three=3, four=4, five='five'
    )
    d['seven'] = 7
    for k in sorted(d.keys()): #ordenado pelas chaves
        print(k, d[k])


if __name__ == '__main__':main()