#!/usr/bin/env python3
"""Generators example"""

def counter():
    yield 1
    yield 2
    yield 3

# Можно использовать в циклах
print('counter gen')
for a in counter():
    print(a)

# Можно использовать с вызовом .next
# При каждом next() генератор возобновляется с места последнего yield
# Когда значения заканчиваются — возбуждается StopIteration
print('counter gen with next')
gen = counter()
while True:
    try:
        value = next(gen)
        print(value)
    except StopIteration:
        break

def subgen():
    yield 'A'
    yield 'B'

def wrapper():
    yield 1
    yield from subgen()
    yield 2

print('wrapper gen')
for a in wrapper():
    print(a)
