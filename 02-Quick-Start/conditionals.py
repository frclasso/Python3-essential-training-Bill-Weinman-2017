#!/usr/bin/python

a, b = 0, 1  #EXPERIMENTEM ALTERAR OS VALORES

if a < b:
    print('a ({}) is less than b ({})'.format(a,b))
else:
    print('a ({}) is grater than b ({})'.format(a,b))


#outra abordagem
print('Menor' if a < b else 'Maior')