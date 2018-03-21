#!/usr/bin/python

import bitstring


def main():
    a =bitstring.BitString(bin = '01010101')
    print(a.hex, a.bin, a.uint)


if __name__ == "__main__":main()