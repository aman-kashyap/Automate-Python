#!/bin/bash/python3

import random

def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'jai shree Ram'
    if answerNumber == 2:
        return 'jai bajrang bali'
    if answerNumber == 3:
        return 'jai ma kali'
    if answerNumber == 4:
        return 'jai mata di'

r = random.randint(1,4)
bolo=getAnswer(r)
print("bolo " +bolo+"!")