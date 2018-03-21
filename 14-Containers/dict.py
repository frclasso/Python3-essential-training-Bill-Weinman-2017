#!/usr/bin/python

x = dict(four=4, five=5, six=6)

d = dict(one=1, two=2, three=3, **x) #inclui o dicionario x no dicionario d

for k, v in d.items():
    print(k, v)