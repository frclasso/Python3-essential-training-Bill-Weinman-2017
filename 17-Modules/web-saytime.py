#!/usr/bin/python

import time, saytime


t = time.localtime()
print("Content-type: text/html\n")
print(
    "Florianopolis City - Santa Catarina Island it is now "+
    saytime.saytime_t(t).words() +
    time.strftime(', on %A, %d %B %Y.')
)