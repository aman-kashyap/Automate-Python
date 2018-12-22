#!/bin/bash/python3

import random

print ("guess a number between 1 and 100")
num=0
r=random.randint(1,100)
guess=0
while num != r:
    print("take a guess")
    guess= guess+1
    num=int(input())
    if num < r:
        print("your guess is too low")
        #print("take a guess")
        #num=int(input())
    elif num >r:
        print("your guess is too high")
        #print("take a guess")
        #num=int(input())
    else:
        print ("you guessed correct! number "+ str(num)+" in " +str(guess)+" tries")