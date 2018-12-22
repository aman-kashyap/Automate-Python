#!/bin/bash/python3

def spam():
    eggs=292929     #local spam
    bacon()
    print(eggs)     #local eggs


def bacon():
    ham=101         #local bacon
    eggs=2          #local bacon
    print(ham)      #local ham
    print(eggs)     #local eggs

eggs=23         #global eggs
spam()
print(eggs)     #global eggs