#!/bin/bash/python3


def number(devidedBy):
    try:
        return 42/devidedBy
    except ZeroDivisionError:
        print("Error: Invalid Argument  zero used as divisor ")


print(number(2))
print(number(0))
print(number(12))
print(number(1))
